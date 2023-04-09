from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from about.models import About
from about.api.serializers import SkillsSerializer 

@api_view(['GET', 'POST'])
def get_skill(request):
    # GET
    if request.method == 'GET':
        skill= About.objects.all()
        if skill:
            serializer = SkillsSerializer(skill, many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
            
        else:
           
            return Response( status=status.HTTP_204_NO_CONTENT)

    # POST

    elif request.method == 'POST':

        
        data = {
            'skill_name': request.data['skill_name'],
            'description': request.data['description'],
            'organization': request.data['organization'],
            'certificaty_URL': request.data['certificaty_URL'],
            'author': request.user.id,
        
        
        }
    
        serializer = SkillsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'api_status':'true',
                'message':'skill Added Successfully',
                'data':serializer.data
            }
            return Response(res,status=status.HTTP_201_CREATED)

        else:
           
            return Response( serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['GET', 'PUT', 'DELETE'])
def get_update_skill(request,id):
    skill=About.objects.get(id=id)
    if request.method == 'GET':
        serialize=SkillsSerializer(skill)
        return Response(serialize.data)
    elif request.method == 'PUT':
         data = {
            'skill_name': request.data['skill_name'],
            'description': request.data['description'],
            'organization': request.data['organization'],
            'certificaty_URL': request.data['certificaty_URL'],
            'author': request.user.id,
        
        }
        
         serialize=SkillsSerializer(skill,data=data)
         if serialize.is_valid():
            serialize.save()
            return Response(serialize.data )
         return Response(serialize.errors , status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
          skill.delete()
          res = {
                'api_status': 'true',
                'message': 'skill Deleted Successfully',
            }
          return Response(res, status=status.HTTP_204_NO_CONTENT)

    
