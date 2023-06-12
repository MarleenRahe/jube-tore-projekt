from django import forms
from django.forms import ModelForm, DateField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Todo

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "details", "date", "user")
        widgets = {
            'details': forms.Textarea(attrs={'rows': 8, 'cols': 26}),
            'user': forms.HiddenInput(),
        }
        labels = {
            "title": 'Nimi',
            "details": 'Märkmed',
            "date": 'Kuupäev'
        }
