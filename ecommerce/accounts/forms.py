from accounts.models import User,Profile
from django import forms
from django.contrib.auth.hashers import make_password

class user_register_form(forms.ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']

    def clean(self):
        c_data=super().clean()
        p1=c_data.get('password1')
        p2=c_data.get('password2')

        if p1 and p2 and p1!=p2:
            raise forms.ValidationError("Passwords don't match ")
        
        return c_data
    
    def save(self,commit=True):
        user=super().save(commit=False)
        user.password=make_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
class profile_form(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['avatar','bio']
