from django.contrib.auth.forms import UserCreationForm
from .models import User, AnnouncementModel
from django.forms import ModelForm,Textarea
from django import forms
from .models import AddressModel,aboutInstractor
from django.contrib.auth.decorators import login_required

class RegistrationForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['email','name','image','AccounType']
        
class addressform(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ['street', 'city', 'state', 'zip', 'country']

class aboutform(forms.ModelForm):
    class Meta:
        model = aboutInstractor
        fields = ['description']

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

