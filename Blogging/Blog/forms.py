from django import forms

from Blog.models import Customer


class RegForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"



