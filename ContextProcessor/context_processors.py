from ProdemyApp.models import CourseCategoryModel
def Categories(request):
    categories = CourseCategoryModel.objects.all()
    return {'Categories': categories}
