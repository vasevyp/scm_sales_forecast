from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
# from django.http import HttpResponse

from .forms import ContactForm

site = 'Sales-Forecast'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'content': content
            })
            # Сообщение для нас, приходит на адрес ['info@sczl.ru']
            send_mail(f'Сообщение от {site}', '..',
                      'info@sczl.ru',
                      ['info@sczl.ru'],
                      html_message=html
                      )
            # Сообщение для отправителя, приходит на адрес [str(email)] укзанный при отправке
            send_mail(f'Сообщение от {site}', 'Ваше сообщение успешно доставлено!\nЭто автоматический ответ, чтобы вы знали, что мы получили ваше сообщение,\nмы свяжемся с вами в ближайшее время.\nСпасибо за ваше обращение!',
                      'info@sczl.ru',
                      [str(email)]
                      )

            return redirect('success_page')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form
    })

# Функция, которая вернет сообщение в случае успешного заполнения формы


def success(request):
    return render(request, 'contact/success.html')
