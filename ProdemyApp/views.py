from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login,logout,authenticate
# Create your views here.

class SigninView(View):
    template_name = "account/register.html"  # Update with the correct template name

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('home')
        else:
            form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

class user_login(View):
    template_name = "account/login.html"
    
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # profile page e redirect korbe    