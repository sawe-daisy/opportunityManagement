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
from .models import User, Account, Opportunity
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

class OpportunityCreateView(CreateView):
    model = Opportunity
    fields = ['image', 'name', 'account', 'user', 'amount', 'stage']
    template_name='accounts/oppForm.html'
    def form_valid(self, form):
        return super().form_valid(form)

class PostListView(ListView):
    model = Account
    template_name = 'index.html'
    context_object_name = 'posts'
    # ordering = ['-pub_date']

class PostDetailView(DetailView):
    def get_object(pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        posts=Opportunity.objects.filter(account=pk)
    
        context={
            'posts': posts
        }
        return render(request, 'accounts/details.html', context)

        return redirect('account')

    # def get_context_data(self, *args, **kwargs):
    #     return get_object_or_404(Account, pk=self.kwargs.get('pk'))
    #     print(stuff)
    #     posts=Opportunity.objects.filter(account=pk)
        
    # model = Opportunity
    # template_name= 'posts/details.html'
    # context='posts'

    
        # total_likes=stuff.total_likes()
        # context["total_likes"]=total_like