from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core import serializers


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        newUser = User(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'))
        newUser.save()
    return HttpResponse(serializers.serialize("json", [newUser]))
