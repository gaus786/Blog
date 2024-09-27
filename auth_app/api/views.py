from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
from rest_framework import status
from auth_app.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from django.shortcuts import render



# @permission_classes([IsAuthenticated])


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
   
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

       
        if serializer.is_valid():
         
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')

          
            if User.objects.filter(username=username).exists():
                return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already in use.'}, status=status.HTTP_400_BAD_REQUEST)

           
            try:
                user = serializer.save()

               
                refresh = RefreshToken.for_user(user)

                return Response({
                    'message': 'Registration successful!',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({'error': 'Registration failed.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        
        username = request.data.get('username')
        password = request.data.get('password')
        print(username, password)

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=400)

        try:
            user = User.objects.get(username=username)
            print(user)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=404)

      
        # auth = authenticate(username=username, password=password)
        # print(auth)
        
        if user.password==password:
        
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful!',
            }, status=200)
        else:
            return Response({'error': 'Invalid password.'}, status=401)
        
        
        
def login_page_view(request):
    return render(request, 'login.html')

def dash_page_view(request):
    return render(request, 'dash.html')

def register_page_view(request):
    return render(request,'register.html')
