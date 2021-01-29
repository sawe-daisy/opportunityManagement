from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from urllib import request
from .models import User, Account
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
    return render(request, 'register.html', context)

class PostCreateView(CreateView):
    model = Account
    fields = ['name', 'user', 'address', 'image']
    template_name='accounts/accountForm.html'
    def form_valid(self, form):
        return super().form_valid(form)

class PostListView(ListView):
    model = Account
    template_name = 'index.html'
    context_object_name = 'posts'
    # ordering = ['-pub_date']

class PostDetailView(DetailView):
    model = Account
    template_name= 'posts/image_detail.html'

    def get_context_data(self, *args, **kwargs):
        context=super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Account, id=self.kwargs['pk'])
        # total_likes=stuff.total_likes()
        # context["total_likes"]=total_likes
        return context