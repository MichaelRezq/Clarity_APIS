from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from permissions import IsAutherOrReadOnly
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.decorators import APIView
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from comments.models import Comment
from comments.api.serializers import CommentSerializer



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
def get_post_problems(request):
    # GET
    if request.method == 'GET':
        query = request.query_params.get('q', '')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            community=request.user.community
        ).order_by('-id')

        if posts:
            serializer = PostSerializer(posts, many=True)
            res = {
                'api_status': 'true',
                'message': 'Posts Fetched Successfully',
                'data': serializer.data,
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            res = {
                'api_status': 'false',
                'message': 'error in fetching problems',
            }
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

    # POST

    elif request.method == 'POST':

        data = {
            'title':request.data['title'],
            'content': request.data['content'],
            'author': request.user.id,
            'community': str(request.user.community),
           
        }

        serializer = PostSerializer(data=data)
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
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        data = {
            'title':request.data['title'],
            'content': request.data['content'],
            'author': request.user.id,
            'community': str(request.user.community),
          
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        post.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

class LikeView(APIView):
    permission_classes = (permissions.IsAuthenticated)
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return Response({'status': 'success'})


@api_view(['GET', 'POST'])
def get_post_comment(request,postid):
    # GET
    post = Post.objects.filter(id=postid)[0]

    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        if comments:
            serializer = CommentSerializer(comments, many=True)
            res = {
                'api_status': 'true',
                'message': 'Comment added  Successfully',
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
            'user': request.user.id,
            'post': post.id,
            'comment': request.data['comment'],
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
            'user': request.user.id,
            'post': post.id,
            'comment': request.data['comment'],

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

