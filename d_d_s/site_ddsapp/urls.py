from django.urls import path
from . import views

app_name = 'site_ddsapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_page/', views.create_page, name='create_page'),
    path('edit_page/', views.edit_page, name='edit_page'),
    
    
]