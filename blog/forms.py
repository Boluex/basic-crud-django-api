from django.forms import ModelForm
from.models import post,comment
from django import forms

class renew(ModelForm):
    title=forms.CharField(required=True)
    content=forms.CharField(required=False)
    image=forms.ImageField(required=False)
    class Meta:
        model=post
        fields=['title','content','image']
        


class reply(ModelForm):
    comment=forms.CharField(required=False)
    image=forms.ImageField(required=False)
    class Meta:
        model=comment
        fields=['comment','image']
        