from django.urls import path
from .views import email
app_name='mail'
urlpatterns=[
    path('',email,name='email')
]

