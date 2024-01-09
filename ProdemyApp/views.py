from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegistrationForm,addressform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .models import CourseModel

from .models import User,AddressModel

from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View, CreateView,ListView
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

from django.contrib.auth import login,logout,authenticate
from .models import CourseModel, AnnouncementModel,CourseCategoryModel, CouponModel
from .forms import AnnouncementForm
from django.urls import reverse_lazy
from django.utils.text import slugify


class SigninView(View):
    template_name = "account/register.html"  # Update with the correct template name

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('login')
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
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

class user_logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class user_profile(View):
    template_name = "account/profile.html"
    
    def get(self, request,pk, *args, **kwargs):
        profile = User.objects.get(id = pk)
        address = User.objects.get(id = pk)
        return render(request, self.template_name, {'profile': profile,'address':address})

class addinfo(View):
    template_name = "account/updateprofile.html"
    
    def get(self, request, *args, **kwargs):
        form = addressform()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = addressform(request.POST)
        print(form)
        if form.is_valid():
            address = form.save(commit=False)
            address.person = request.user
            address.save()
            return redirect('profile',request.user.id)
        else:
            form = addressform()
        return render(request, self.template_name, {'form': form})

class editinfo(View):
    template_name = "account/updateprofile.html"
    
    
    def get(self, request, *args, **kwargs):
        address = AddressModel.objects.get(person = request.user)
        form = addressform(instance = address)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        address = AddressModel.objects.get(person = request.user)
        form = addressform(request.POST,instance = address)
        print(form)
        if form.is_valid():
            address = form.save(commit=False)
            address.person = request.user
            address.save()
            return redirect('profile',request.user.id)
        else:
            form = addressform()
        return render(request, self.template_name, {'form': form})


          
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



class CategoryView(ListView):
    model = CourseCategoryModel
    template_name = 'views/category_list.html'
    context_object_name = 'Categories'
    
class CreateCategoryView(CreateView):
    model = CourseCategoryModel
    template_name = 'views/create_category.html'
    fields = ('name',)
    success_url = reverse_lazy('category')
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)

# class CategoryTopDownView(ListView):
#     model = CourseCategoryModel
#     template_name = 'base.html'
#     context_object_name = 'Categories'

class CategoryDetailsView(View):
    template_name = 'views/category_details.html'  
    model = CourseCategoryModel
    
    
    def get(self, request, slug):
        category = get_object_or_404(CourseCategoryModel, slug=slug) 
        course = CourseModel.objects.filter(category=category)
        Categories = CourseCategoryModel.objects.all()
        context = {'category': category, 'Courses' : course, 'Categories' : Categories}
        return render(request, self.template_name, context)