
from django.urls import path
from . import views

urlpatterns = [
    
    path('contact/',views.contact, name = "homepage"),
    path('about/', views.about, name = "ab"),
    path('forms/', views.forms, name =  "forms"),
    path('djangoform/', views.djangoForm, name = "DJF" ),
    # path('student/',views.studentform, name = "std"),
    path('student/',views.passwordValidation, name = "std"),
    
    
]