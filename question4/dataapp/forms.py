from django import forms
from dataapp.models import *

class candidateForm(forms.ModelForm):
    class Meta:
        model=candidate
        fields='__all__'
        widgets={
        'Name':forms.TextInput(attrs={'class':'form-control'}),
        'Email':forms.TextInput(attrs={'class':'form-control'}),
        'Address':forms.Textarea(attrs={'class':'form-control'}),
        'first_round':forms.TextInput(attrs={'class':'form-control'}),
        'second_round':forms.TextInput(attrs={'class':'form-control'}),
        'third_round':forms.TextInput(attrs={'class':'form-control'}),
        }

class candidateForm_1(forms.ModelForm):
    class Meta:
        model=candidate
        fields=('address',)
        widgets={
          'Address':forms.Textarea(attrs={'class':'form-control'}),
        }
