from django.urls import path
from . import views

app_name = 'site_ddsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_page/', views.create_page, name='create_page'),
    path('edit_page/', views.edit_page, name='edit_page'),
    path('list_status/', views.list_status, name='list_status'),
    path('list_type/', views.list_type, name='list_type'),
    path('list_category/', views.list_category, name='list_category'),
    path('create_status/', views.create_status, name='create_status'),
    path('directory_management/', views.directory_management, name='directory_management'),
    path('create_type/', views.create_type, name='create_type'),
    path('create_category/', views.create_category, name='create_category'),
    
    
    
]