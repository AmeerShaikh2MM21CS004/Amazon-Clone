from django import forms

class userForm(forms.Form):
    val1=forms.CharField(label="Username",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    val2=forms.CharField(label="Password",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))