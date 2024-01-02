from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, RANKING


class PersonModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    account_type = models.CharField(choices=ACCOUNT_TYPE)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='/profile_pictures', blank=True, null=True)
    rank = models.CharField(choices=RANKING, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
class AddressModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
class CouseCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='/category_thumnail', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class CourseModel(models.Model):
    category = models.ForeignKey(CouseCategoryModel, on_delete=models.CASCADE)
    instructor = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='/course_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class MyCourseModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    is_Completed = models.BooleanField(default=False)

class AnnouncementModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='/announcement_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BlogPostModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='/blog_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class BlogCommentModel(models.Model):
    comment_by = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPostModel, on_delete=models.CASCADE)
    comment = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class AssignmentModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='/assignment_files', blank=True, null=True)
    deadline = models.DateTimeField()
    
class AssignmentSubmissionModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='/assignment_submission_files', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class QuestionModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='/question_files', blank=True, null=True)
    
class MCQModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    
class CertificateModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='/certificate_template', blank=True, null=True)
    achived_at = models.DateTimeField(auto_now_add=True)
    
class PaymentModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    
class CouponModel(models.Model):
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    coupon_code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    
    
class FeedbackModel(models.Model):
    person = models.ForeignKey(PersonModel, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    feedback = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)