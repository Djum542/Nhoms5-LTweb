from django import forms
class loginform(forms.Form):
    user = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20, widget = forms.PasswordInput)