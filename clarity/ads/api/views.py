from rest_framework import generics, filters,permissions
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
import os
from rest_framework import request, status, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from ads.models import  Ads,Review
from .serializers import  AdsSerializer,ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def get_post_ads(request):
    # GET
    if request.method == 'GET':
        query_type = request.query_params.get('type', '')
        query_search = request.query_params.get('search', '')

        ads = Ads.objects.filter(
            Q(type__icontains=query_type) , Q(name__icontains=query_search)| Q(description__icontains=query_search) )
            # community=request.user.community).order_by('-id')
        pwd = os.getcwd()
        if ads:
            serializer = AdsSerializer(ads, many=True)
            res = {
                'api_status': 'true',
                'message': 'Ads Fetched Successfully',
                'data': serializer.data,
                'pathImage': pwd
            }
            return Response(res,status=status.HTTP_200_OK)
        else:
            res = {
                'api_status': 'false',
                'message': 'error in fetching ads',
            }
            return Response(res, status=status.HTTP_204_NO_CONTENT)

    # POST

    elif request.method == 'POST':

        data = {
            'name': request.data['name'],
            'description': request.data['description'],
            'image': request.FILES['image'],
            'type': request.data['type'],
            'siteUrl': request.data['siteUrl'],
            'country': request.data['country'],
            'region': request.data['region'],
            'street': request.data['street'],
            'services': request.data.getlist('services'),
            'author': request.user.id,
        }

        serializer = AdsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'Ads Added Successfully',
                'data':serializer.data
            }
            return Response(res,status=status.HTTP_201_CREATED)

        else:
            res = {
                'api_status': 'false',
                'message': 'error in add ads',
                'data': serializer.errors
            }
            return Response(res,status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', 'PUT', 'DELETE'])
def get_edit_delete_ads(request, pk):
    try:
        ads = Ads.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = AdsSerializer(ads)
        res = {
            'api_status': 'true',
            'message': 'Ads Fetched Successfully',
            'data': serializer.data,
        }
        return Response(res)

    # PUT
    elif request.method == 'PUT':
        data={
            'name': request.data['name'],
            'description': request.data['description'],
            'image': request.FILES['image'],
            'type': request.data['type'],
            'siteUrl': request.data['siteUrl'],
            'country': request.data['country'],
            'region': request.data['region'],
            'street': request.data['street'],
            'services': request.data['services'],
            'author': request.user.id,
        }

        serializer = AdsSerializer(ads, data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status': 'true',
                'message': 'Ads Updated Successfully',
                'data': serializer.data
            }
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        ads.delete()
        res = {
            'api_status': 'true',
            'message': 'Ads Deleted Successfully',
        }
        return Response(res, status=status.HTTP_204_NO_CONTENT)

# view functions for rate and review
@api_view(['POST'])
def add_review(request, pk):
    try:
        ad = Ads.objects.get(pk=pk)
    except:
        return Response({'error': 'Ad not found'}, status=status.HTTP_404_NOT_FOUND)

    data = {
        "ad":pk,
        "user":request.user.id,
        "rating":request.data['rating'],
        "comment": request.data['comment'],
    }

    # check if the user has already reviewed the ad
    if Review.objects.filter(ad=ad, user=request.user).exists():
        return Response({'error': 'You have already reviewed this ad'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

        # update ad total_ratings and total_stars fields
        ad.total_ratings = Review.objects.filter(ad=ad).count()
        ad.total_stars += serializer.validated_data['rating']
        ad.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_review(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except:
        return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
