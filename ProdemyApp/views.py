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
            return redirect('home')
          
def teacherDashboard(request):
    return render(request, 'account/teacherDashboard.html')


def certificate_view(request):
    context = {
        'learner_name': 'Obaydul Hasan Nayeem',
        'course_title': 'Introduction to Django',
        'issue_date': 'January 4, 2024',
        'instructor_name': 'Saiful Islam',
    }

    return render(request, 'account/certificate.html', context)

# from django.shortcuts import render, get_object_or_404
# from django.template.loader import render_to_string
# import weasyprint  # Or ReportLab, as preferred
# from .models import MyCourseModel

# def generate_certificate(request, learner_id, course_id):
#     # learner = get_object_or_404(Learner, pk=learner_id)
#     learner = "Nayeem"
#     course = get_object_or_404(MyCourseModel, pk=course_id)

#     # Fetch template (example using a default template)
#     template_html = render_to_string("certificate.html", {
#         "learner_name": learner.name,
#         "course_title": course.title,
#         "completion_date": course.completion_date,
#         # ... other data
#     })

#     # Render PDF
#     html = weasyprint.HTML(string=template_html)
#     pdf = html.write_pdf()

#     # Store PDF and send email (details omitted for brevity)
