from django.contrib import admin
from .models import Information

# Register your models here.


# Register your models here.
@admin.register(Information)
class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'course']
