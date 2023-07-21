
from django.urls import path
from . import views

urlpatterns = [
    
    path('contact/',views.contact, name = "homepage"),
    path('about/', views.about, name = "ab"),
    
]