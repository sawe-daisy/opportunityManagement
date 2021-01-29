from django.shortcuts import render
from django.shortcuts import render
from urllib import request
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets
from django.template import loader 
from .models import User
from rest_framework.decorators import permission_classes
from django.http import Http404
from rest_framework.views import APIView
from .forms import RegistrationForm
import json
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from itertools import chain
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
    context={
        'form':form,
    }
    # return loader.render_to_string(request, 'register.html', 'index.html', context)
    return render(request, 'index.html', context)