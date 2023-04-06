from rest_framework import generics, filters,permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from posts.api.views import CustomPagination
from rest_framework import request, status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from problems.models import  Problem,Solution\
    # ,Like
from .serializers import  ProblemSerializer,SolutionSerializer,ProblemSerializerGet,SolutionSerializerGet
    # ,LikeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_post_problems(request,pk=None):
    # GET
    # if pk:
    #     problem = get_object_or_404(Problem, pk=pk)
    #     problem.views += 1
    #     problem.save()
    #     serializer = ProblemSerializer(problem)
    #     return Response(serializer.data)

    if request.method == 'GET':
        query = request.query_params.get('q', '')
        problems = Problem.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            community=request.user.community
        ).select_related('author').order_by('-id')
        total_answer = Solution.total_solution(request.user.community)
        total_problems = Problem.total_problems(request.user.community)
        tags = []
        allTags = Problem.objects.all().distinct()
        for p in allTags:
            tags.append(p.tags)
        unique_tags = list(set([item for sublist in tags for item in sublist]))
        if problems:
            serializer = ProblemSerializerGet(problems, many=True)
            res = {
                'api_status': 'true',
                'message': 'Problems Fetched Successfully',
                'data': serializer.data,
                'total_answer':total_answer,
                'total_problems':total_problems,
                'all_tags':unique_tags
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
        # title=request.data['title']
        # desc=request.data['description']
        # author = request.user
        # tags=request.data['tags']
        # community = request.user.community
        # problem = Problem.objects.create(title=title,description=desc,author=author,tags=tags,community=community)
        # serializer = ProblemSerializer(problem,many=False)
        print('========================',request.user.id)
        data = {
            'title': request.data['title'],
            'description': request.data['description'],
            'image': None,
            'tags': request.data['tags'],
            'body': request.data['body'],
            'author': request.user.id,
            'author_name': request.user.username,
            'community': str(request.user.community),
            # 'num_answer':
        }

        serializer = ProblemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'Problem Added Successfully',
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


# 3.1 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def get_edit_delete_problem(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
        num_answers = problem.get_num_of_answer()
        problem.increment_views(request)  # Increment views count for this problem

    except Problem:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = ProblemSerializerGet(problem)
        res = {
            'api_status': 'true',
            'message': 'Problem Fetched Successfully',
            'data': serializer.data,
            'num_answers':num_answers
        }
        return Response(res)

    # PUT
    elif request.method == 'PUT':
        data = {
            'title': request.data['title'],
            'description': request.data['description'],
            'image': None,
            'tags': request.data['tags'],
            'body': request.data['body'],
            'author': request.user.id,
            'author_name': request.user.username,
            'community': str(request.user.community),
        }

        serializer = ProblemSerializer(problem, data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status': 'true',
                'message': 'Problem Updated Successfully',
                'data': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        problem.delete()
        res = {
            'api_status': 'true',
            'message': 'Problem Deleted Successfully',
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def get_post_solution(request,problemID):
    # GET
    problem = Problem.objects.filter(id=problemID)[0]

    if request.method == 'GET':
        solutions = Solution.objects.filter(problem=problem)
        if solutions:
            serializer = SolutionSerializerGet(solutions, many=True)
            res = {
                'api_status': 'true',
                'message': 'Solutions Fetched Successfully',
                'data': serializer.data
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            res = {
                'api_status': 'false',
                'message': 'No solutions yet',
            }
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)

    # # POST
    elif request.method == 'POST':
        data = {
            'user': request.user.id,
            'problem': problem.id,
            'solution': request.data['solution'],
            'user_name':request.user.username,
            'community': str(request.user.community),

        }

        serializer = SolutionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'Solution Added Successfully',
                'data':serializer.data
            }
            return Response(res,status=status.HTTP_201_CREATED)

        else:
            res = {
                'api_status': 'false',
                'message': 'error in add solution',
                'data': serializer.errors
            }
            return Response(res,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', 'PUT', 'DELETE'])
def get_edit_delete_solution(request, problemID,solutionID):
    try:
        problem = Problem.objects.get(pk=problemID)
        solution = Solution.objects.get(pk=solutionID)
    except Problem:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = SolutionSerializer(solution)
        res = {
            'api_status': 'true',
            'message': 'Solution Fetched Successfully',
            'data': serializer.data
        }
        return Response(res)

    # PUT
    elif request.method == 'PUT':
        data = {
            'user': request.user.id,
            'problem': problem.id,
            'solution': request.data['solution'],

        }

        serializer = SolutionSerializer(solution, data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status': 'true',
                'message': 'Solution Updated Successfully',
                'data': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        solution.delete()
        res = {
            'api_status': 'true',
            'message': 'Solution Deleted Successfully',
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)


class LikeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, post_id):
        solution = get_object_or_404(Solution, id=post_id)
        user = request.user
        if user in solution.likes.all():
            solution.likes.remove(user)
        else:
            solution.likes.add(user)
        return Response({'status': 'success'})
