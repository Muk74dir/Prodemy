from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from .constans import ACCOUNT_TYPE

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    AccounType = models.CharField(choices=ACCOUNT_TYPE,max_length = 20)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

 
class AddressModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
class CouseCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to='media/category_thumnail', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class CourseModel(models.Model):
    category = models.ForeignKey(CouseCategoryModel, on_delete=models.CASCADE)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='media/course_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class MyCourseModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    is_Completed = models.BooleanField(default=False)

class AnnouncementModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/announcement_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BlogPostModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='media/blog_thumnail', blank=True, null=True)
    
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class BlogCommentModel(models.Model):
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPostModel, on_delete=models.CASCADE)
    comment = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class AssignmentModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='media/assignment_files', blank=True, null=True)
    deadline = models.DateTimeField()
    
class AssignmentSubmissionModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/assignment_submission_files', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class QuestionModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='media/question_files', blank=True, null=True)
    
class MCQModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)
    
class CertificateModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/certificate_template', blank=True, null=True)
    achived_at = models.DateTimeField(auto_now_add=True)
    
class PaymentModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
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
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    feedback = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)