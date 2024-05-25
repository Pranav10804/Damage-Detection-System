from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit, name='submit'),
    path('image/', views.image, name='image'),
]