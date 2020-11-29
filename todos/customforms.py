from .models import Todo
from django.forms.models import ModelForm

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = [
            'title',
            'status',
        ]