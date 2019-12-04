from django import forms

clas LoginForm(forms.Form):
username = forms.CharField()
password = forms.CharField(widget.PasswordInput())

