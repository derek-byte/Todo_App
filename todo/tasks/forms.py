from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    # To add a placeholder in the task input form
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Task
        # Import everything in this file
        fields = '__all__'