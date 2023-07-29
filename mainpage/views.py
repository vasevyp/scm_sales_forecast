from django.shortcuts import render


def index(requiest):
    return render(requiest, 'mainpage/index.html')
