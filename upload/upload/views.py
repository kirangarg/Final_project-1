# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from demoupload.forms import SignUpForm
from django.contrib.auth.hashers import make_password
from demoupload.models import UserModel

# Create your views here.
def signup_view(request):
    #logic
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # save data to database
            new_user = UserModel(username=username, name=name,email=email, password=make_password(password))
            new_user.save()
    elif request.method == 'GET':
        form = SignUpForm()
        #display signup form
        #today = datetime.now()
    return render(request, 'signup.html', {'form': form})




