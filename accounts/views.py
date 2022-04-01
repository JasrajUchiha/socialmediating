from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #reverse_lazy is used to take you to a certain page on success and on failure, lazy part is added so that it only activates when someone actually submits the form
    template_name = "accounts/signup.html"
