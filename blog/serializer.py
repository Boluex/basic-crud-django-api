from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from.models import post,comment


class homeserializer(ModelSerializer):
    author=SerializerMethodField('get_author')
    image=SerializerMethodField('get_image')
    class Meta:
        model=post
        fields=['id','title','content','author','date_posted','image']
    def get_author(self,post):
        return post.author
    def get_image(self,post):
        return post.image
    
class createserializer(ModelSerializer):
    class Meta:
        model=post
        fields=['title','content','date_posted']
        
class commentcreateserializer(ModelSerializer):
    class Meta:
        model=comment
        fields=['comment','date_posted']
    
class commentserializer(ModelSerializer):
    author=SerializerMethodField('get_author')
    image=SerializerMethodField('get_image')
    post=SerializerMethodField('get_post')
    class Meta:
        model=comment
        fields=['id','comment','author','date_posted','image','post']
    def get_author(self,comment):
        return comment.author
    def get_image(self,comment):
        return comment.image
    def get_post(self,comment):
        return comment.post



