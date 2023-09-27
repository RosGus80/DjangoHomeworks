from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('ChangeDate', 'date')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        forbidden = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
                     'обман', 'полиция', 'радар']

        if any(x in cleaned_data for x in forbidden):
            raise forms.ValidationError('Проверьте название на наличие запрещенных на сайте слов')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'




