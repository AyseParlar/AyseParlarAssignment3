from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    courses = models.ManyToManyField('Course', related_name='students', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Course(models.Model):
    teacher = models.ForeignKey('Teacher')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    classroom = models.CharField(max_length=10)
    times = models.TextField()

    def __str__(self):
        if self.students.count():
            return self.name + ' // STUDENTS=[' + (', '.join(map(str, self.students.all()))) + ']'
        else:
            return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    office_details = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
