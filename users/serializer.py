from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField
from.models import profile
from django.contrib.auth.models import User

class profileserializer(ModelSerializer):
    username=SerializerMethodField('get_user')
    image=SerializerMethodField('get_image')
    email=SerializerMethodField('get_email')
    class Meta:
        model=profile
        fields=['username','image','number','nickname','age','email']
        
    def get_user(self,profile):
        return profile.user.username
    def get_email(self,profile):
        return profile.user.email
    def get_image(self,profile):
        return profile.image
    
class registerserializer(ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['username','password','password2','email']
        
    def save(self):
        pass1=self.validated_data['password']
        pass2=self.validated_data['password2']
        email=self.validated_data['email']
        username=self.validated_data['username']
        new_user=User(username=username,email=email)
        if pass1 == pass2:
            new_user.set_password(pass1)
            new_user.save()
        raise ValueError('password does not match')