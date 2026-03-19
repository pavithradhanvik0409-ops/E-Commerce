from django import forms

from .models import Category, Product


class SearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all()
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all()
    )