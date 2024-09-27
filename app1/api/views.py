from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializer import PostSerializer
from rest_framework import status
from app1.models import Post_detail
from django.contrib.auth import authenticate
from auth_app.models import User
from django.shortcuts import render


@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def create_post(request):
    if request.method == 'POST':
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_all_posts(request):
    if request.method=='GET':
       
        posts = Post_detail.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def get_user_posts(request,user):
    if request.method=='GET':
        posts = Post_detail.objects.filter(user=user)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    
    
def getpost_page(request):
    return render(request, 'dash.html')    
        
    

        
        

        