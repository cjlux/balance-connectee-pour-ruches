from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authentication.models import User

class SignupForm(UserCreationForm):
  
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class LoginForm(forms.Form):
      email     = forms.EmailField(max_length=63, 
                                   widget=forms.EmailInput(attrs={'cols': 80, 'rows': 20}), 
                                   label_suffix=' ',
                                   label='Mail utilisateur',
                                   required=True)
      password  = forms.CharField(max_length=63, 
                                  label_suffix=' ',
                                  widget=forms.PasswordInput(attrs={'cols': 80, 'rows': 20}), 
                                  label='Mot de passe', 
                                  required=True)
    
