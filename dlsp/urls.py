from django.urls import path
from . import views

app_name = 'dlsp'

urlpatterns = [
    path('', views.index, name='index'),
    path('admission/', views.admission, name='admission'),
    path('programs/', views.programs, name='programs'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
]