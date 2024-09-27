# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

from auth_app.api.views import registration_view, login_page_view

urlpatterns = [
    # JWT token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    path('register/', views.register_page_view, name='register_page'), 
    path('login/', views.login_page_view, name='login_page'),  # Render login page
    path('api/login/', views.login_view, name='login_api'),    # API for login
    
    path('dash/',views.dash_page_view, name='dash'), 
    # Auth-related endpoints
    path('register/', registration_view, name='register'),  
    
]

