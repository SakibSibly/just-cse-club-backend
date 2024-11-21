from django.db import models


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
