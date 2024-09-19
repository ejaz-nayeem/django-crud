from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'address', 'phone', 'designation', 'salary', 'description']
    salary = forms.IntegerField()
    phone= forms.IntegerField()
class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "address",
            "phone",
            "description",
            'salary',
            'designation'
        ]
    phone= forms.IntegerField()
    salary=forms.IntegerField(disabled=True)
    designation=forms.CharField(max_length=200, disabled=True)

        
    
    #description = forms.CharField(widget=forms.TextInput)