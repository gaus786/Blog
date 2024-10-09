from django.urls import path


from app1.api.views import create_post,get_all_posts,get_user_posts,like_post,create_post_page
from . import views

urlpatterns = [

    
    # Auth-related endpoints
    path('api/createpost/', create_post, name='create_post'),  
    path('createpost/', create_post_page, name='post'), 
     
    path('api/getpost/', get_all_posts, name='allpost'),
    path('getpost/',views.getpost_page,name='getpost'),
    
    path('userpost/<int:user>',get_user_posts, name='userpost'),
    
    path('api/like/',like_post,name='likepost'),

]