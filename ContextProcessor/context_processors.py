from ProdemyApp.models import CourseCategoryModel, CourseModel, User
def Categories(request):
    categories = CourseCategoryModel.objects.all()
    return {'Categories': categories}

def Course(request):
    courses = CourseModel.objects.all()
    for course in courses:
        print(course.title)
    return {'courses':courses}

def Users(request):
    users = User.objects.all()
    return {'users':users}