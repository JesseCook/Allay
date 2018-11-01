from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #widgets = {
         #   'username': forms.TextInput(attrs={'class': 'usernameClass', 'placeholder' : 'username'}),
         #   'email' : forms.EmailInput(attrs={'class': 'emailClass', 'placeholder' : 'email'}),
         #   'password1' : forms.PasswordInput(attrs={'class': 'pass1Class', 'placeholder' : 'password'}),
         #   'password2' : forms.PasswordInput(attrs={'class': 'pass2Class', 'placeholder' : 're-enter password'}),
        #}
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'usernameClass', 'placeholder' : 'username'})
        self.fields['username'].label = ''
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'emailClass', 'placeholder' : 'email'})
        self.fields['email'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password1'].label = ''
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'pass1Class', 'placeholder' : 'password',})
        self.fields['password2'].label = ''
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'pass2Class', 'placeholder' : 'password confirmation',})
