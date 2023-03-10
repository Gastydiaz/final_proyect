from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from users.models import UserProfile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    
    
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['first_name','last_name']


class UserProfileForm(forms.ModelForm):

    phone = forms.FloatField(label='Telefono')
    birth_date = forms.DateField(label='Fecha de nacimiento')
    profile_picture = forms.ImageField(label='Foto de perfil',required=False)
    class Meta:
        model = UserProfile
        fields = ['phone', 'birth_date', 'profile_picture']