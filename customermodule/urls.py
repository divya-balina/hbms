from django.contrib import admin
from django.urls import path,include
from . import views
from .views import topdestinations, review_list, add_review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viewrooms/',views.viewrooms,name='viewrooms'),
    path('bookrooms/',views.bookrooms,name='bookrooms'),
    path('list/',views.roomdetails_list,name='roomdetails_list'),
    path('topdestinations/',topdestinations, name='topdestinations'),
    path('',review_list,name='review_list'),
    path('add/',add_review,name='add_review'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)