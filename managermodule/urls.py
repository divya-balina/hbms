from django.contrib import admin
from django.urls import path,include

from . import views
app_name = 'managermodule'

urlpatterns = [
    path('addrooms/',views.addrooms,name='addrooms'),
    path('add_room_details/',views.add_room_details,name='add_room_details'),
    path('view/',views.view_roomdetails,name='view_roomdetails'),
    path('insert/', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),




]