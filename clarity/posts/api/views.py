from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from permissions import IsAutherOrReadOnly
from posts.models import Post
from .serializers import PostSerializer,PostSerializerForGet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import APIView
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from comments.models import Comment
from comments.api.serializers import CommentSerializer,CommentSerializerForGet



# Set the pagination parameters
class CustomPagination(PageNumberPagination):
    page_size = 10  # Number of results per page
    page_size_query_param = 'page_size'  # Query parameter to override `page_size`
    max_page_size = 100  # Maximum number of results per page


# ------------------- POSTS -------------------

# List all posts or create a new post
# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     pagination_class = CustomPagination
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'content']  # Specify the fields to search
#     ordering_fields = ['title', 'created_at']  # Specify the fields to order by
    # authentication_classes=[TokenAuthentication]
    # permission_classes = [IsAuthenticated]

# Retrieve, update or delete a post instance
# class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes=[TokenAuthentication]
#     permission_classes = [IsAutherOrReadOnly]


@api_view(['GET', 'POST'])
def get_post_problems(request,pk=None):
    
    # GET
    if request.method == 'GET':
        query = request.query_params.get('q', '')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            community=request.user.community
        ).order_by('-id')

        if posts:
            serializer = PostSerializerForGet(posts, many=True)
            res = {
                'api_status': 'true',
                'message': 'Posts Fetched Successfully',
                'data': serializer.data,
            }
            # print(res)
            return Response(res,status=status.HTTP_200_OK)
        else:
            res = {
                'api_status': 'false',
                'message': 'error in fetching posts',
            }
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

    # POST

    elif request.method == 'POST':

        # data = {
        #     'title':request.data['title'],
        #     'content': request.data['content'],
        #     
        #     'author': request.user.id,
        #     'community': str(request.user.community),
        # }

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'Post Added Successfully',
                'data':serializer.data
            }
            return Response(res,status=status.HTTP_201_CREATED)

        else:
            res = {
                'api_status': 'false',
                'message': 'error in add problem',
                'data': serializer.errors
            }
            return Response(res,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET','PUT','DELETE'])
def get_spesific_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        # data = {
        #     'content': request.data['content'],
        #     'author': request.user.id,
        #     'community': str(request.user.community),
          
        # }
        serializer = PostSerializer(instance=post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        post.delete()
        return Response({'sucsess': f'{request.user.username} Your Post Deleted successfully' },status= status.HTTP_204_NO_CONTENT)
    

class LikeView(APIView):
    # permission_classes = (permissions.IsAuthenticated)
    def post(self, request, post_id):
        print("---------user-----",post_id)
        user = request.user
        print("---------user-----",user)

        post = get_object_or_404(Post, id=post_id)

        print("---------post.likes.all()-----",post.likes.all())
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'sucsess': f'like removed by  {request.user.username}' },status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'sucsess': f'like added by  {request.user.username}'}, status=status.HTTP_200_OK)

class ShareView(APIView):
    # permission_classes = (permissions.IsAuthenticated)
    def post(self, request, post_id):

        print("---------user-----",post_id)
        user = request.user
        print("---------user-----",user)

        post = get_object_or_404(Post, id=post_id)
        # 1 add the user to the field of the sharedby
        post.shared_by.add(user)

        # 2 add the post to the user who share
        post_shared=Post.objects.get(id=post_id)
        print("-----------------post image -------------",post_shared.image)
        

        data = {
            'content': post_shared.content,
            'author': request.user.id,
            'community': str(request.user.community),
            'title':'null',
        }
        if post_shared.image:
            data['image'] = post_shared.image
            print("``````````````````````````````````hello form test for youssef")
        if post_shared.video:
            data['video'] = post_shared.video
        serializer = PostSerializer(data=data)
        print("data---------------------------------------",data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response({'sucsess': f'{request.user.username} You Shared The POst Successfully'}, status=status.HTTP_200_OK)



        return Response({'sucsess': f'{request.user.username} You Shared The POst Successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_post_comment(request,postid):
    # GET
    post = Post.objects.filter(id=postid)[0]

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        if comments:
            serializer = CommentSerializerForGet(comments, many=True)
            res = {
                'api_status': 'true',
                'message': 'Comment fetched  Successfully',
                'data': serializer.data
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            res = {
                'api_status': 'false',
                'message': ' No Comment ',
            }
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

    # # POST
    elif request.method == 'POST':
        data = {
            'author': request.user.id,
            'post': post.id,
            'content': request.data['content'],
            'community': str(request.user.community),

        }

        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'Comment Added Successfully',
                'data':serializer.data
            }
            return Response(res,status=status.HTTP_201_CREATED)

        else:
            res = {
                'api_status': 'false',
                'message': 'error in add Your Comment',
                'data': serializer.errors
            }
            return Response(res,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', 'PUT', 'DELETE'])
def get_edit_delete_comment(request, postid,commentid):
    try:
        post = Post.objects.get(pk=postid)
        comment = Comment.objects.get(pk=commentid)
    except post:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        res = {
            'api_status': 'true',
            'message': 'comment returned Successfully',
            'data': serializer.data
        }
        return Response(res)

    # PUT
    elif request.method == 'PUT':
        data = {
            'author': request.user.id,
            'post': post.id,
            'content': request.data['content'],
            'community': str(request.user.community),
        }

        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status': 'true',
                'message': 'comment Updated Successfully',
                'data': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        comment.delete()
        res = {
            'api_status': 'true',
            'message': 'comment Deleted Successfully',
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)

