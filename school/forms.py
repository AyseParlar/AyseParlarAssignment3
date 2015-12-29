from django import forms

from school.models import *


class RegistrationForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    student = forms.ModelChoiceField(queryset=Student.objects.all())

    def save(self, commit=True):
        self.cleaned_data['student'].courses.add(self.cleaned_data['course'])

