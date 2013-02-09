# -*- coding: utf-8 -*-
from django import forms

errors = {
    'required': u'не заполнено',
    'invalid': u'введено не верное значение',
    'max_length': (u'слишком длинно'),
    'min_length': (u'минимум 4 символа'),
}

min_length = 3

class SingupForm(forms.Form):
    login = forms.CharField(max_length=100, min_length=min_length,error_messages=errors)
    email = forms.EmailField(error_messages=errors)
    password = forms.CharField(widget=forms.PasswordInput,error_messages=errors)


class SigninForm(forms.Form):
    login = forms.CharField(max_length=100, min_length=min_length,error_messages=errors)
    password = forms.CharField(widget=forms.PasswordInput,error_messages=errors)
   
