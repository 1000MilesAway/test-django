from django import forms
from .models import Image
from django.core.exceptions import ValidationError


class AddImage(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('img', 'img_url', )


class ResizeImage(forms.Form):
    width = forms.IntegerField(label='Ширина', required=False)
    height = forms.IntegerField(label='Высота', required=False)

    def clean(self):
        data = self.cleaned_data
        width = data.get('width')
        height = data.get('height')
        if not width and not height:
            raise ValidationError("Заполните как минимум одно поле")
