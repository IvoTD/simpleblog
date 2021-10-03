from django.views import generic
from members.forms import SignUpForm, EditProfileForm, PasswordChanged
from django.contrib.messages.api import success
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm,UserChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

def password_success(request):
    return render(request, 'registration/password_success.html', {})
    

class ChangePassword(PasswordChangeView):
    form_class = PasswordChanged
    success_url = reverse_lazy('password_success')

#NOT WORKING 
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

# def register(request):
#     if request.method == 'POST':
#         f = SignUpForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('login')
#     else:
#         f = SignUpForm()
#     return render(request, 'registration/register.html', {'form': f})

class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


