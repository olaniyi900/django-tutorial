from django import forms

class TodoForm(forms.Form):
    text = forms.CharField()