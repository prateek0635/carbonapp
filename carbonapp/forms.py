from django import forms 
  
class profile(forms.Form): 
    name = forms.CharField() 
    geeks_field = forms.ImageField() 