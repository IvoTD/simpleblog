from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields

class PasswordChanged(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter your old password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter your new password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Confirm new password'})) 

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # profile_image = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    #select the field and give them a bootstrap class
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        #we can remove the fields on the page by removing any of the following:
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'date_joined')
