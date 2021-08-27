from pathlib import WindowsPath
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=True)
    message = forms.CharField(widget = forms.Textarea,required=True)