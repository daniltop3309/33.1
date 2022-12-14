from django.shortcuts import render, redirect
from polls.forms import *
from django.http import HttpResponse, HttpResponseRedirect


def reg(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return HttpResponse(f"""
{name}, поздравляю с регистрацией!
Указанные вами данные: Имя - {name}, Email - {email}, Пароль - {password}
""")
    return render(request, 'reg.html', {'form': form})


def login(request):
    userformlog = UserFormLog()
    if request.method == 'POST':
        userformlog = UserFormLog(request.POST)
        if userformlog.is_valid():
            name = userformlog.cleaned_data['name']
            password = userformlog.cleaned_data['password']
            if name == 'User1' and password == '12345678':
                return HttpResponse(f"""Поздравляю с успешным входом, {name}""")
            else:
                return redirect('reg')
    else:
        return render(request, 'login.html', {'userformlog': userformlog})

