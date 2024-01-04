from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
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
        '''
        user = form.save(commit=False)
        if user.email == 'sifat.sbs@gmail.com':
            user.is_staff = True  # Set is_staff to True to make the user a staff member
            user.save()
        '''
        return render(request, self.template_name, {'form': form})


def teacherDashboard(request):
    return render(request, 'account/teacherDashboard.html')