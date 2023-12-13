# tasks/forms.py

from django import forms
try:
    from .models import Task
    print(' Imported Task ')
except ImportError as e:
    print(repr(e))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title','description','is_completed']



    
