from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcomePage, name = 'welcomePage'),
    path('home/',views.home, name = 'home'),
    path('motivation/',views.send_motivation_email, name = 'motivation'),
    
]

