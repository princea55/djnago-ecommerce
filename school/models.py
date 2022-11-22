from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=60, blank=False)
    address = models.TextField(max_length=255, blank=True)
    CITIES = (
        ('ahmedabad', 'Ahmedabad'),
        ('surat', 'Surat'),
        ('rajkot', 'Rajkot'),
    )
    city = models.CharField(max_length=255, choices=CITIES, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, blank=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=50, blank=False)
    subject_id = models.ForeignKey(Subject, blank=False, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def next_by_code():
    student = Student.objects.all().order_by('id').last()
    if student:
        return f'S{datetime.today().year}-{int(student.student_code.split("-")[1]) + 1}'
    else:
        return f'S{datetime.today().year}-1'


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False)
    student_code = models.CharField(max_length=50, blank=False, unique=True, default=next_by_code)
    email = models.EmailField(max_length=60, blank=False)
    CITIES = (
        ('ahmedabad', 'Ahmedabad'),
        ('surat', 'Surat'),
        ('rajkot', 'Rajkot'),
    )
    city = models.CharField(max_length=255, choices=CITIES, blank=False)
    age = models.IntegerField(blank=True, null=True)
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=255, choices=GENDER, blank=False)
    dob = models.DateField(blank=False)
    join_date = models.DateField(blank=True)
    phone = PhoneNumberField(blank=False, unique=True)
    section = models.CharField(max_length=2, blank=True)
    active = models.BooleanField(default=True)
    school_id = models.ForeignKey(School, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class_id = models.ForeignKey(StudentClass, blank=False, on_delete=models.CASCADE)
    skil = models.ManyToManyField(
        Skill,
        verbose_name=_("Skills"),
        blank=True,
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"))

    def __str__(self):
        return self.name


def next_by_code_teacher():
    teacher = Teacher.objects.all().order_by('id').last()
    if teacher:
        return f'T{datetime.today().year}-{int(teacher.teacher_code.split("-")[1]) + 1}'
    else:
        return f'T{datetime.today().year}-1'


class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False)
    teacher_code = models.CharField(max_length=50, blank=False, unique=True, default=next_by_code_teacher,
                                    editable=False)
    email = models.EmailField(max_length=60, blank=False)
    CITIES = (
        ('ahmedabad', 'Ahmedabad'),
        ('surat', 'Surat'),
        ('rajkot', 'Rajkot'),
    )
    city = models.CharField(max_length=255, choices=CITIES, blank=False)
    age = models.IntegerField(blank=True, null=True)
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(max_length=255, choices=GENDER, blank=False)
    dob = models.DateField(blank=False)
    join_date = models.DateField(blank=True)
    phone = PhoneNumberField(blank=False, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skil = models.ManyToManyField(
        Skill,
        verbose_name=_("Skills"),
        blank=True,
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"))

    def __str__(self):
        return self.name
