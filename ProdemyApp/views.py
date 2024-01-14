from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View,TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RegistrationForm,addressform,AnnouncementForm,aboutform
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

from .models import CourseModel

from .models import User,AddressModel, MCQModel

from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import View, CreateView,ListView
from .forms import RegistrationForm, MCQForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

from django.contrib.auth import login,logout,authenticate
from .models import CourseModel, AnnouncementModel,CourseCategoryModel, CouponModel,aboutInstractor
from .forms import AnnouncementForm
from django.urls import reverse_lazy
from django.utils.text import slugify
import requests

# for transaction
from django.http import HttpResponse 
from django.views.generic import View, TemplateView, DetailView
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Transaction
from .sslcommerz import sslcommerz_payment_gateway

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
    
    def get(self, request, *args, **kwargs):
        about = aboutInstractor.objects.filter(person = request.user)
        if about:
            about = aboutInstractor.objects.get(person = request.user)
            address = AddressModel.objects.filter(person = request.user)
            return render(request, self.template_name, {'profile': request.user,'address':address,'about':about})
        form = aboutform()
        address = AddressModel.objects.filter(person = request.user)
        return render(request, self.template_name, {'profile': request.user,'address':address,'form':form})
    
    def post(self, request, *args, **kwargs):
        form = aboutform(request.POST)
        if form.is_valid():
            about = form.save(commit=False)
            about.person = request.user
            about.save()
            return redirect('profile')
        else:
            form = aboutform()
        return render(request, self.template_name, {'form': form})
    
class editAbout(View):
    template_name = "account/profile.html"
    
    def get(self, request, *args, **kwargs):
        about = aboutInstractor.objects.get(person = request.user)
        form = aboutform(instance = about)
        return render(request, self.template_name, {'profile': request.user,'form':form})
    
    def post(self, request, *args, **kwargs):
        about = aboutInstractor.objects.get(person = request.user)
        form = aboutform(request.POST,instance = about)
        print(form)
        if form.is_valid():
            about = form.save(commit=False)
            about.person = request.user
            about.save()
            return redirect('profile')
        else:
            form = aboutform()
        return render(request, self.template_name, {'form': form})

class addinfo(View):
    template_name = "account/updateprofile.html"
    
    def get(self, request, *args, **kwargs):
        form = addressform()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = addressform(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.person = request.user
            address.save()
            return redirect('profile')
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
            return redirect('profile')
        else:
            form = addressform()
        return render(request, self.template_name, {'form': form})


def teacherDashboard(request):
    return render(request, 'account/teacherDashboard.html')

def certificate_view(request):
    context = {
        'learner_name': request.user.name,
        'email': request.user.email,
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
    
# for transactions ---------------------------
class Index(TemplateView):
    template_name = "transactions/index.html"

def DonateView(request):
    # name = request.POST['name']
    name = request.user.name
    # amount = request.POST['amount']
    amount = '6500'
    return redirect(sslcommerz_payment_gateway(request, name, amount))


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'mainsite/carts/checkout-success.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse('nothing to see')

    def post(self, request, *args, **kwargs):

        data = self.request.POST

        try:
            Transaction.objects.create(
                name = data['value_a'],
                tran_id=data['tran_id'],
                val_id=data['val_id'],
                amount=data['amount'],
                card_type=data['card_type'],
                card_no=data['card_no'],
                store_amount=data['store_amount'],
                bank_tran_id=data['bank_tran_id'],
                status=data['status'],
                tran_date=data['tran_date'],
                currency=data['currency'],
                card_issuer=data['card_issuer'],
                card_brand=data['card_brand'],
                card_issuer_country=data['card_issuer_country'],
                card_issuer_country_code=data['card_issuer_country_code'],
                verify_sign=data['verify_sign'],
                verify_sign_sha2=data['verify_sign_sha2'],
                currency_rate=data['currency_rate'],
                risk_title=data['risk_title'],
                risk_level=data['risk_level'],

            )
            messages.success(request,'Payment Successful')

        except:
            messages.success(request,'Something Went Wrong')
        return render(request, 'transactions/success.html')


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'transactions/faild.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)





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
    right = 0
    wrong = 0

    if request.user.is_authenticated:
        if request.method == "POST":
            questions = MCQModel.objects.all()
            total = len(questions)
            for question in questions:
                selected = request.POST.get(f"option_{question.id}")
                if selected == question.answer:
                    right += 1
                else:
                    wrong += 1

            return render(request, 'account/mcq_result.html', {'right': right, 'wrong': wrong, 'total':total})

        questions = MCQModel.objects.all()
        
        return render(request, 'account/mcq.html', {'questions': questions})

    return redirect('login')

def result(request):
    return render(request, 'account/mcq_result.html')