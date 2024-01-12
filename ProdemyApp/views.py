from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View, CreateView
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login,logout,authenticate
from .models import CourseModel, AnnouncementModel, MCQModel, User
from .forms import AnnouncementForm,MCQForm
from .globals import lst

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


class VideoPlayerView(CreateView):
    template_name = 'views/player.html'
    context = {}
    
    def get(self, request, id):
        course = CourseModel.objects.get(id=id)
        self.context['course'] = course
        return render(request, self.template_name, self.context)

def Announcement(request):
     if request.method == 'POST':
        form = AnnouncementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('teacherDashboard')
     else:
        form = AnnouncementForm()
     return render(request, 'account/create_announcement.html', {'form': form})


def MyCourses(request):
    announcements = AnnouncementModel.objects.all()
    return render(request, 'account/mycourses.html', {'announcements': announcements})


def DeleteAnnouncement(request, announcement_id):
    announcement = get_object_or_404(AnnouncementModel, id = announcement_id)
    announcement.delete()
    return render(request, 'account/mycourses.html')



def mcq(request):
    mcq_questions = MCQModel.objects.all()
    form = MCQForm(request.POST)
    return render(request, 'account/mcq.html', {'mcq_questions': mcq_questions})

def results(request):
    return render(request, 'account/mcq_result.html')

def create_mcq(request):
    if request.method == 'POST':
        form = MCQForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            option1 = form.cleaned_data['option1']
            option2 = form.cleaned_data['option2']
            option3 = form.cleaned_data['option3']
            option4 = form.cleaned_data['option4']
            answer = form.cleaned_data['answer']
            ques = MCQModel(
                question=question,
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                answer=answer
            )
            ques.save()
            print(ques)
            return redirect('mcq')
    form = MCQForm()
    return render(request, 'account/create_mcq.html', {'form': form})


    
def mcq(request):
    if request.user.is_authenticated:
        questions = MCQModel.objects.all()
        for q in questions:
            lst.append(q.id)
            print(lst)
        response = render(request, 'account/mcq.html', {'questions': questions})
        response.set_cookie('questions', ','.join(map(str, lst)))
        return response
    return redirect('results')




def result(request):
    if request.method == 'POST':
        # Assuming lst is defined and contains question IDs
        questions = MCQModel.objects.filter(pk__in=lst)
        total_questions = len(lst)
        score = 0
        wrg = 0

        for q in questions:
            selected_option = request.POST.get(str(q.id))  # Use the question ID as the key
            print(selected_option)
            print(q.question)
            if selected_option == q.answer:
                score += 1
            else:
                wrg += 1

        context = {
            'cur_score': score,
            'cur_wrong': wrg,
            'total_questions': total_questions,
        }

        return render(request, 'account/mcq_result.html', context)
    else:
        return redirect('mcq')