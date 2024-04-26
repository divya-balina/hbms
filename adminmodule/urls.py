from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name= 'homepage'),
    path('managerhomepage/',managerhomepage,name='managerhomepage'),
    path('customerhomepage/',customerhomepage,name='customerhomepage'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('login1/',login1,name='login1'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contact/',contact,name='contact'),
    path('contactmail/',contactmail,name='contactmail'),
    path('aboutus/',aboutus,name='aboutus'),
]