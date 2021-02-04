from django import forms
from user.models import *

class userinfo_form(forms.ModelForm):
    class Meta:
        model =userinfo
        fields='__all__'
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(attrs={'class':'form-control'}),
        'street':forms.TextInput(attrs={'class':'form-control'}),
        'pincode':forms.TextInput(attrs={'class':'form-control'}),
        'country':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),
        'phoneno':forms.TextInput(attrs={'class':'form-control'}),
        }
