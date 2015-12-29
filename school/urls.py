from django.conf.urls import url
from school import views

urlpatterns = [
    url(r'^students/$', views.StudentListView.as_view()),
    url(r'^teachers/$', views.TeacherListView.as_view()),
    url(r'^courses/$', views.CourseListView.as_view()),
    url(r'^add_student/$', views.StudentCreateView.as_view()),
    url(r'^add_teacher/$', views.TeacherCreateView.as_view()),
    url(r'^add_course/$', views.CourseCreateView.as_view()),
    url(r'^add_registration/$', views.RegistrationCreateView.as_view()),
]