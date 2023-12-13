from django.db import models
from django.contrib import admin
# Create your models here.

class TaskAdmin(admin.ModelAdmin):
    print('Within TaskAdmin')
    list_display = ('title','description','date_created','is_completed')
    search_fields = ('title',)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300,unique=False,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
    
