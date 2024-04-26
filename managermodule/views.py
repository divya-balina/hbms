from django.shortcuts import render


def addrooms(request):
    return render(request, 'managermodule/addrooms.html')

def add_room_details(request):
    if request.method == 'POST':
        no_of_rooms = request.POST.get('no_of_rooms')
        type_of_room = request.POST.get('type_of_room')
        noofpeople = request.POST.get('noofpeople')

        roomdetails_obj = roomdetails(
            no_of_rooms=no_of_rooms,
            type_of_room=type_of_room,
            noofpeople=noofpeople
        )
        roomdetails_obj.save()

        return render(request, 'managermodule/datainserted.html')

    return render(request, 'managerhomepage.html')

def view_roomdetails(request):
    return render(request,'managermodule/view_roomdetails.html')


def viewrooms(request):
    return render(request,'managermodule/viewrooms.html')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee

def insert_emp(request):
    if request.method == "POST":
        EmpId = request.POST['EmpId']
        EmpName = request.POST['EmpName']
        EmpGender = request.POST['EmpGender']
        EmpEmail = request.POST['EmpEmail']
        EmpDesignation = request.POST['EmpDesignation']
        data = Employee(EmpId=EmpId, EmpName=EmpName, EmpGender=EmpGender, EmpEmail=EmpEmail,
                        EmpDesignation=EmpDesignation)
        data.save()

        return redirect('show-emp')
    else:
        return render(request, 'INSERT.html')
from django.contrib.auth.decorators import login_required

def show_emp(request):
    employees = Employee.objects.all()
    return render(request, 'SHOW.html', {'employees': employees})

# Update Employee

def edit_emp(request,pk):
    employees = Employee.objects.get(id=pk)
    if request.method == 'POST':
            print(request.POST)
            employees.EmpName = request.POST['EmpName']
            employees.EmpGender = request.POST['EmpGender']
            employees.EmpEmail = request.POST['EmpEmail']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.EmpDesignation = request.POST['EmpDesignation']
            employees.save()
            return redirect('show-emp')
    context = {
        'employees': employees,
    }

    return render(request,'EDIT.html',context)

#Delete Employee
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee

def remove_emp(request, pk):
    try:
        employee = get_object_or_404(Employee, id=pk)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found", status=404)

    if request.method == 'POST':
        employee.delete()
        return redirect('show-emp')

    context = {
        'employee': employee,
    }

    return render(request, 'DELETE.html', context)








