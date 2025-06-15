from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name




from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True )  # New field
    college_name = models.CharField(max_length=200,null=True, blank=True )  # New field
    course = models.CharField(max_length=100,null=True, blank=True)        # New field
    branch = models.CharField(max_length=100)        # New field
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


