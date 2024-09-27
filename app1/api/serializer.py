from rest_framework import serializers
from app1.models import Post_detail


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post_detail
        fields = '__all__'
        
        
        
    