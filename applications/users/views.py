from django.shortcuts import render
from django.views.generic.edit import FormView,View
# Create your views here.
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
class LoginUsuer(FormView):

    template_name = "user/login.html"
    form_class=LoginForm
    success_url = reverse_lazy("condominio:condominioHome")
    
    def form_valid(self,form):
        user= authenticate(
            username= form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request,user)
        return super(LoginUsuer,self).form_valid(form)

class Logout(View):
    def get(self,request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy("Users:login"))
        