from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(requests):
    return render(requests, 'index.html', {})


def blog(requests):
    return render(requests, 'blog.html', {})


def about(requests):
    return render(requests, 'about.html', {})


def contact(requests):
    if requests.method == "POST":
        message_name = requests.POST['message-name']
        message_email = requests.POST['message-email']
        textarea = requests.POST['textarea']

        # Send an email
        send_mail(
            'message from ' + message_name, #subject
            textarea, #message
            message_email, #from email
            ['djangotest62@gmail.com'], #to email
        )

        return render(requests, 'contact.html', {'message_name': message_name})

    else:
        return render(requests, 'contact.html', {})
