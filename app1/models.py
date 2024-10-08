from django.db import models
from auth_app.models import User

# Create your models here.


class Post_detail(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
# class Like(models.Model):
#     post = models.ForeignKey(Post_detail, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     like=models.IntegerField(default=0)
    
#     def __str__(self):
#         return self.like
    
