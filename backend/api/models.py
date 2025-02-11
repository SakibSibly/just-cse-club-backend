from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    city = models.CharField(null=True, max_length=50)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.CASCADE)
    profile_pic = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Regular user, not staff by default
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + ' - ' + self.otp


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    serial_number = models.IntegerField()
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # image = models.ImageField(upload_to='faculty_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", related_name="blogs")
    read_time = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50] + '...'


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    funding_goal = models.IntegerField(default=0)
    current_funding = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    registered = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    full_description = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="events")
    image_url = models.TextField()
    # image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Donation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    trxID = models.CharField(max_length=20)
    ref = models.CharField(max_length=50)
    purpose = models.TextField()
    add_info = models.TextField(null=True, blank=True)


## Needs more work
# class Transaction(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     amount = models.IntegerField(default=0)
#     type = models.CharField(max_length=10, choices=[
#         ('income', 'Income'),
#         ('expense', 'Expense')
#     ])
#     reference = models.ForeignKey(to=[
#         ('event', Event),
#         ('notice', Notice),
#     ], on_delete=models.CASCADE)
#     date = models.DateTimeField()


# class Gallery(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     # image = models.ImageField(upload_to='gallery_images/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


class Feedback(models.Model):
    name = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    message = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.username


# class About(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
