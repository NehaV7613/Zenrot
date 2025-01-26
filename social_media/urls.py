# social_media/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check-access/', views.check_access, name='check_access'),
]
