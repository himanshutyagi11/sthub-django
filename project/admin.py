from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

admin.site.register(Student)

from django.contrib import admin
from .models import Contact

admin.site.register(Contact)
