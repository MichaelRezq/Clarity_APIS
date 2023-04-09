from django.shortcuts import render, redirect
from rest_framework import generics, filters, permissions, status
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from jobs.models import Job
from django.db.models import Q

from rest_framework.response import Response


@api_view(['GET', 'POST'])
def job_list(request):
    if request.method == 'GET':
        query = request.query_params.get('q', '')
        job_type = request.query_params.get('job_type')
        position = request.query_params.get('position')
        skills = request.query_params.get('skills')
        jobs = Job.objects.filter(Q(title__icontains=query) | Q(description__icontains=query),
                                  comunity=request.user.community)

        if job_type:
            jobs = jobs.filter(job_type=job_type)
        if position:
            jobs = jobs.filter(position=position)
        if skills:
            skills_list = skills.split(",")
            for skill in skills_list:
                jobs = jobs.filter(skills__icontains=skill)

        serialize = JobSerializer(jobs, many=True)
        return Response(serialize.data)
    elif request.method == 'POST':
        print("POOOOOOOOOOOOOOOOst")
        data = {
            "title": request.data["title"],
            "company": request.data["company"],
            "description": request.data["description"],
            "Responsibilities": request.data["Responsibilities"],
            "Qualification": request.data["Qualification"],
            "salary": request.data["salary"],
            "Experience": request.data["Experience"],
            "position": request.data["position"],
            "skills": request.data["skills"],
            "country": request.data["country"],
            "region": request.data["region"],
            "city": request.data["city"],
            "postcode": request.data["postcode"],
            "full_address": request.data["full_address"],
            "job_type": request.data["job_type"],
            # "location": request.data["location"],
            "url": request.data["url"],
            # "comunity":request.data["comunity"],
            "comunity": str(request.user.community),
            "author": request.user.id
        }
        serialize = JobSerializer(data=data)
        if serialize.is_valid():
            print('allllid')
            serialize.save()
            res={
                'api_status':'true',
                'data':serialize.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def job_one(request, id):
    job = Job.objects.get(id=id)
    if request.method == 'GET':
        serialize = JobSerializer(job)
        return Response(serialize.data)
    elif request.method == 'PUT':
        data = {
            "title": request.data["title"],
            "company": request.data["company"],
            "description": request.data["description"],
            "Responsibilities": request.data["Responsibilities"],
            "Qualification": request.data["Qualification"],
            "salary": request.data["salary"],
            "Experience": request.data["Experience"],
            "position": request.data["position"],
            "country": request.data["country"],
            "region": request.data["region"],
            "city": request.data["city"],
            "postcode": request.data["postcode"],
            "full_address": request.data["full_address"],
            "job_type": request.data["job_type"],
            # "location": request.data["location"],
            "url": request.data["url"],
            # "comunity":request.data["comunity"],
            "comunity": request.user.community,
            "author": request.user.id
        }
        serialize = JobSerializer(job, data=data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

