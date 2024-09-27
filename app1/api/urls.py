from django.urls import path


from app1.api.views import create_post,get_all_posts,get_user_posts

urlpatterns = [

    
    # Auth-related endpoints
    path('createpost/', create_post, name='post'),  
    path('getpost/', get_all_posts, name='allpost'),
    path('userpost/<int:user>',get_user_posts, name='userpost'),

]