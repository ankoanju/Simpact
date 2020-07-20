from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='simpact-home'),
    path('businessLogin', views.businessLogin, name='business-login'),
    path('npoLogin', views.npoLogin, name='npo-login'),
    path('about', views.simpactAbout, name='simpact-about'),
    path('volunteerDescription' , views.volunteerDescription, name='volunteer-description'),
    path('volunteerDashboard' , views.volunteerDashboard, name='volunteer-dashboard')
    
    
    #path('', views.InsertPerks)
]
