from django.shortcuts import render
from django.views.generic import TemplateView
from ProdemyApp.views import CourseCategoryModel

class MyTemplateView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request):
        Categories = CourseCategoryModel.objects.all()
        context = {'Categories':Categories}
        return render(request, self.template_name, context)
    