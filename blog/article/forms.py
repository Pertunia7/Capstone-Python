from django import forms



class InputForm(forms.form):
    
    name= forms.CharField()
    email = forms.EmailField()
    