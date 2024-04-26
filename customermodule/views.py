from django.shortcuts import render, redirect

from .models import TouristReview
from .forms import ReviewForm

def viewrooms(request):
    return render(request,'customermodule/viewrooms.html')

def bookrooms(request):
    return render(request,'customermodule/bookrooms.html')


def topdestinations(request):
    return render(request,'topdestinations.html')


def roomdetails_list():
    return None

def review_list(request):
    if request.method== 'GET':
        reviews=TouristReview.objects.all()
        return render(request,'reviewpage.html',{'reviews':reviews})

def add_review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review=form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('review_list')
        else:
            form =ReviewForm()
        return render(request,'reviewpage.html',{'form':form})
