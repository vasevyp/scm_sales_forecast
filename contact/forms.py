from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255,  label='Имя*')
    email = forms.EmailField(label='E-mail*')
    phone = forms.CharField(required=False, label='Телефон',
                            widget=forms.TextInput(attrs={'placeholder': ' желательно добавить телефон'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 50, 'rows': 7}), label='Сообщение*')
    captcha = CaptchaField()
