from django import forms


class TestForm(forms.Form):
    name = forms.CharField(max_length=64)
    birthday = forms.DateTimeField()
