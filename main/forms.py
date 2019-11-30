from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(label='name', max_length=30)
    pin = forms.CharField(label='pin', max_length=10)
    cgpa = forms.DecimalField(label='cgpa', max_digits=3, decimal_places=2)

    class Meta:
        model = Student
        fields = ['name', 'pin', 'cgpa']

class DeleteStudentForm(forms.ModelForm):
    name = forms.CharField(label = 'name', max_length=30)

    class Meta:
        model = Student
        fields = ['name']