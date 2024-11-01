from django import forms
from .models import Task, StudentList, Contact


class Task_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']
    # Register_Number = forms.CharField(max_length=10, min_length=10, label="Student ID",
    #                              error_messages={
    #                                  'required': 'Student ID is required',
    #                                  'min_length': 'Student ID must be exactly 10 characters',
    #                                  'max_length': 'Student ID must be exactly 10 characters'
    #                              })
    # Name = forms.CharField(max_length=100, label="Student Name",
    #                                error_messages={'required': 'Student name is required'})


class UploadFileForm(forms.Form):
    file = forms.FileField()

# forms.py
from django import forms

class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'name', 'email', 'phone_number', 'address']