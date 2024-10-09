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
    user=request.user.id
    data = request.data
    data['user'] = user
    # print(data)
    
    if request.method == 'POST':
        serializer=PostSerializer(data=request.data)

        if serializer.is_valid():
        
            serializer.save()
            
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_all_posts(request):
    if request.method=='GET':
       
        posts = Post_detail.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def like_post(request):
    print("user: %s" % request.user.id)
   
    
    post_id = request.data.get('post_id')  
    # print(post_id)

    try:
        post = Post_detail.objects.get(id=post_id)  # Get the post
        # print(post.likes)
    except Post_detail.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

    print(request.data['post_id'])
    if post.likedby.filter(id=request.user.id).exists():
      
        post.likes -= 1
        post.likedby.remove(request.user.id)
        post.save()
        return Response({'message': 'Post unliked', 'likes': post.likes}, status=200)
    else:
      
        post.likes += 1
        post.likedby.add(request.user.id)
        post.save()
        return Response({'message': 'Post liked', 'likes': post.likes}, status=200)
        
        
        
        
        
          
@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def get_user_posts(request,user):
    if request.method=='GET':
        posts = Post_detail.objects.filter(user=user)
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    
    
def getpost_page(request):
    return render(request, 'dash.html')    
        
def create_post_page(request):
    return render(request, 'create_post.html')
    

        

        

        