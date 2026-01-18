from django import forms
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