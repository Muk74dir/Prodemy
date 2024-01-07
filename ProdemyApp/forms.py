from django.contrib.auth.forms import UserCreationForm
from .models import User, AnnouncementModel
from django.forms import ModelForm,Textarea


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

