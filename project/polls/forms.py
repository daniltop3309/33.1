from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'field', 'placeholder': 'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'field','placeholder': 'password'}))


class UserFormLog(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'field'}))
