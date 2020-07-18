from django import forms
from django.forms import ValidationError

class Login_form(forms.Form):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    pwd=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

class Register_Form(forms.Form):
    fname=forms.CharField(label="First name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    lname=forms.CharField(label="Last name",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter last Name'}))
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    pwd=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    cpwd=forms.CharField(label="Password Confirmation",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter Password'}))
    
    def clean(self):
        form_data=self.cleaned_data
        if form_data.get('pwd')==form_data.get('cpwd'):
            print(form_data)
            return form_data
        else:
            raise ValidationError("Password Dosent Match")