from django.shortcuts import render_to_response


# Create your views here.
from django.views.generic import CreateView, ListView, FormView

from school.forms import RegistrationForm
from school.models import *


def home(request):
    return render_to_response('home.html')


class StudentCreateView(CreateView):
    success_url = '/school/students/'
    template_name = 'form_template.html'
    model = Student
    fields = ['first_name', 'last_name', 'email']


class TeacherCreateView(CreateView):
    success_url = '/school/teachers/'
    template_name = 'form_template.html'
    model = Teacher
    fields = ['first_name', 'last_name', 'office_details', 'phone', 'email']


class CourseCreateView(CreateView):
    success_url = '/school/courses/'
    template_name = 'form_template.html'
    model = Course
    fields = ['teacher', 'name', 'code', 'classroom', 'times']


class RegistrationCreateView(FormView):
    success_url = '/school/courses/'
    template_name = 'form_template.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        return super(RegistrationCreateView, self).form_valid(form)


class StudentListView(ListView):
    template_name = 'list_template.html'
    model = Student


class TeacherListView(ListView):
    template_name = 'list_template.html'
    model = Teacher


class CourseListView(ListView):
    template_name = 'list_template.html'
    model = Course

