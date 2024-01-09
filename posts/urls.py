from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post/<str:alit>',views.post,name='post')
    
    

]