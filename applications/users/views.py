from django.shortcuts import render
from django.views.generic.edit import FormView,View,CreateView
# Create your views here.
from .forms import LoginForm
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .models import User
class LoginUsuer(FormView):

    template_name = "user/login.html"
    form_class=LoginForm
    success_url = reverse_lazy("condominio:condominioHome")
    
    def form_valid(self,form):
        user= authenticate(
            username= form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request,user,backend='django.contrib.auth.backends.ModelBackend')
        return super(LoginUsuer,self).form_valid(form)
class registerView(FormView):

    template_name = "user/register.html"
    model=User
    form_class = RegisterForm
    success_url = "/"
    def form_valid(self,form):
        User.objects._create_user(form.cleaned_data['username'],form.cleaned_data['password'],form.cleaned_data['email'],form.cleaned_data['nombre'],form.cleaned_data['empresa'],False,False,form.cleaned_data['tipo'])
        return super(registerView,self).form_valid(form)
class Logout(View):
    def get(self,request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("Users:login"))
        