from django.conf.urls import url
from django.urls import path
# from members import views
from . import views
from members.views import UserEdit, UserRegisterView, ChangePassword
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url for register function
    #url(r'^register/$', views.register, name='register'), 
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    #url for register class
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name= 'registration/change-password.html')),
    path('password/', ChangePassword.as_view(template_name= 'registration/change-password.html')),
    path('password_success', views.password_success, name='password_success'),
]