from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser, UserManager

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class User(AbstractUser):
    email = models.EmailField(max_length=120, unique=True, error_messages={
                              'unique': "Email already exists!"})
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    mobile_no = models.CharField(max_length=20, default=None, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, blank=True, null=True)
    objects = UserManager()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
    
    
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    def __str__(self):
        return self.title