from django.contrib.auth.forms import UserCreationForm
from .models import User, AnnouncementModel,MCQModel
from django.forms import ModelForm,Textarea
from django.contrib.auth import forms
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['email','name','AccounType']
   

class AnnouncementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        
        self.fields['person'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['course'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['title'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['image'].widget.attrs.update({'class': 'form-control mb-2'})
        
    class Meta:
        model = AnnouncementModel
        fields = ['person', 'course', 'title', 'description', 'image']
        widgets = {
            'description': Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }
        labels = {
                'Person' : ('Select Person'),
                'Course' : ('Select Course'),
                'title' : ('Write Announcement Title'),
                'description' : ('Write Announcement Description'),
                'image' : ('Add Announcement Image')
            }
class MCQForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MCQForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['option1'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['option2'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['option3'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['option4'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['answer'].widget.attrs.update({'class': 'form-control mb-2'})
    class Meta:
        model = MCQModel
        fields = ['question' , 'option1', 'option2', 'option3', 'option4', 'answer']
        labels = {
                'question' : ('Write Question'),
                'option1' : ('Write Option 1'),
                'option2' : ('Write Option 2'),
                'option3' : ('Write Option 3'),
                'option4' : ('Write Option 4'),
                'answer' : ('Write Answer'),
            }