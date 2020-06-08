from django import forms

class UserInfoForm(forms.Form):
    
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    mobile = forms.CharField(max_length=12)
    address = forms.CharField(widget=forms.Textarea)