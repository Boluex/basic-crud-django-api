from django.urls import path
from.import api_views
# from. import views
urlpatterns=[
    path('',api_views.home,name='home'),
    path('create/',api_views.create,name='create'),
    path('about/',api_views.about,name='about'),
    path('add_comment/<int:id>',api_views.add_comment,name='add_comment'),
    path('detail/<int:id>',api_views.detail,name='detail'),
    path('delete/<int:id>',api_views.delete,name='delete'),
    path('destroy/<int:id>',api_views.destroy,name='destroy'),
    path('update/<int:id>',api_views.update,name='update'),
    path('update_comment/<int:id>',api_views.update_comment,name='updates'),
    path('comments/<int:id>',api_views.comments,name='comment'),
]