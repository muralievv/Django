from django import forms
from .models import Category
from .models import Tag

black_list = [
    'Nigger'
]
class ProductForm(forms.Form):
    title = forms.CharField(max_length=50, min_length=2)
    description = forms.CharField(max_length=1000)
    salary = forms.IntegerField(required=False)
    photo = forms.ImageField(required=False)

    def clean_date(self):
        name = self.cleaned_data.get('title')
        if name in black_list:
            raise forms.ValidationError('This name is not allowed')
        return name

class SearchForm(forms.Form):
    salary_list = [("1", "меньше 100"), ("2", "больше 100"), ("?", "рандом")]
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    salary = forms.ChoiceField(choices=salary_list, required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),required=False)