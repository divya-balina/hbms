from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
import string




# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def managerhomepage(request):
    return render(request,'managerhomepage.html')

def customerhomepage(request):
    return render(request,'customerhomepage.html')


from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'homepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        pass2= request.POST['password']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
        else:
            messages.info(request,'password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'homepage.html')

from . models import *
def contact(request):
    return render(request,'contact.html')

from django.core.mail import mail_admins

def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend=comment +'-------------------this is just '
        data=feedback1(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>Thank you for giving feedback</center></h1>")

from django.shortcuts import render

def aboutus(request):
    context = {
        'title': 'About Us - Hotel AIRA',
        'mission': 'Our mission is to provide a seamless and enjoyable booking experience for our customers while helping hotels manage their bookings efficiently.',
        'offerings': [
            'Easy hotel booking process',
            'Secure payment options',
            'Real-time availability updates',
            'Customer support 24/7',
            'Integration with various hotel management systems'
        ],
        'team': [
            {'name': 'Balina Divya sri', 'role': 'Team lead'},
            {'name': 'P.Satwika', 'role': 'Team mate'},
            {'name': 'K.Nandini', 'role': 'Team mate'},

        ],
        'contact_email': 'hotelaira@gmail.com'
    }
    return render(request, 'aboutus.html', context)
