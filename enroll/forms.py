from django import forms
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password','message']
        labels = {'name':'Full Name'}
        widgets = {
            'name':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter Your name...'}),
            'email':forms.TextInput(attrs= {'class':'form-control','placeholder':'Enter Your Email...'}),
            'password':forms.PasswordInput(render_value=True,attrs= {'class':'form-control','placeholder':'Enter Your Password...'}),
            'message':forms.TextInput(attrs= {'class':'form-control','placeholder':'Ask Something...'}),
        }
