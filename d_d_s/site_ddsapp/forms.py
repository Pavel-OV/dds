from django import forms  
from .models import Status, Type, Category, Subcategory, Record_dds
from django.utils.translation import gettext as _

# class Status(forms.ModelForm):
#     class Meta:
#         model = Status
#         fields = ['status']
#         widgets ={
#             'status': forms.TextInput(attrs={'size': 100})
#         }
