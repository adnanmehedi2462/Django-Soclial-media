from re import template
from django.urls import path
from .import views 
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    # path('register/',register.as_view(),name="register"),
  
    path('register/',views.register, name='register'),
    path('userlogin/',views.userlogin, name='userlogin'),
    path('logout/',views.userlogout, name='logout'),
     
    path('profile/',profile.as_view(),name="profile"),
    path('editprofile/',views.editprofile, name='editprofile'),
    # mailviewurl
    path('reset/password/',PasswordResetView.as_view(template_name="reset_password.html"), name='password_reset'),
    
    path('reset/password/done/',PasswordResetDoneView.as_view(template_name="reset_password_done.html"), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name="password_reset_complate.html"), name='password_reset_complete'),

    
  	
]
