from django import forms

from proj.models import Img


class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('Изображение', 'Название')
#внутри созданного forms.py создаем форму