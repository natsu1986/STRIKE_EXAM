from django.forms import ModelForm
from .models import task

class taskcreationForm(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'urgent', 'important']
        

