
from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as Auth_Views


urlpatterns = [
   
    path('',views.home),
  
    
    path('logout/',views.Logout,name='logout'),
   
    path('signup/',views.SignUp,name='signup'),
    path('profile/',views.profile),
    path('Signin/',views.Signin,name='signin'),
    path('changepass/',views.user_change_form,name='changepass'),
    path('password_confirm/<uidb64>/<token>/',Auth_Views.PasswordResetConfirmView.as_view(template_name="App/password-reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset/',Auth_Views.PasswordResetView.as_view(template_name='App/password_reset.html'),name="password_reset"),
    path('password-reset-complete/',Auth_Views.PasswordResetCompleteView.as_view(template_name='App/password_reset_complete.html'),name='password_reset_complete'),
    path('password_reset/done/',Auth_Views.PasswordResetDoneView.as_view(template_name='App/password_reset_done.html'),name='password_reset_done'),
    path('MyAccount/',views.Myaccount,name='MyAccount'),
    path('Account/Verify/',views.AccountVerify,name='verify')
]
