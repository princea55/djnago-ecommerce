from django.shortcuts import render, redirect
from .models import School, Subject, StudentClass, Student, Teacher, Skill
from .forms import TeacherForm
from django.db.models.query import QuerySet
from django.db.models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .middleware.main import BlockMobileMiddleware, auth_middleware


# Create your views here.


def index(request):
    return render(request, 'base.html')


@login_required
def teachers_list(request):
    teachers = Teacher.objects.all()
    data = {
        'teachers': teachers
    }
    return render(request, 'school/teachers-list.html', data)


@login_required
def update_teacher(request, id):
    if request.method == 'GET':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(instance=teacher)
        return render(request, 'school/update_teacher.html', {'form': form})
    elif request.method == 'POST':
        teacher = Teacher.objects.get(pk=id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers-list')
        return render(request, 'school/update_teacher.html', {'form': form})


@login_required
def update_student_record(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        mobile_number = request.POST['mobile_number']
        city = request.POST['city']
        gender = request.POST['gender']
        dob = request.POST['dob']
        join_date = request.POST['join_date1']
        student_class = request.POST['class']
        school = request.POST['school']
        Student.objects.update_or_create(pk=id, defaults={
            'name': name,
            'email': email,
            'age': age,
            'phone': mobile_number,
            'city': city,
            'gender': gender,
            'dob': convert_str_to_date(dob),
            'join_date': convert_str_to_date(join_date),
            'class_id': StudentClass.objects.get(pk=int(student_class)),
            'school_id': School.objects.get(pk=int(school)),
        })
        return redirect('students')


@login_required
def update_student(request, id):
    if request.method == 'GET':
        update_student = Student.objects.get(pk=id)
        student_class = StudentClass.objects.all()
        schools = School.objects.all().order_by('name')
        data = {
            'student_class': student_class,
            'schools': schools,
            'update_student': update_student,
            'cities': ['ahmedabad', 'surat', 'rajkot'],
            'gender_list': ['male', 'female', 'other'],
        }
        return render(request, 'school/create_student.html', data)


@login_required
def delete_student(request, id):
    if request.method == 'GET':
        Student.objects.get(pk=id).delete()
        return redirect('students')



@login_required
def create_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST) or None
        if form.is_valid():
            form.save()
            return redirect('create-teacher')
    else:
        form = TeacherForm()
    return render(request, 'school/create_teacher.html', {'form': form})


def convert_str_to_date(date):
    return datetime.datetime.strptime(datetime.datetime.strptime(date, "%m/%d/%Y").strftime('%Y/%m/%d'),
                                      "%Y/%m/%d").date()


@login_required
def create_students(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        mobile_number = request.POST['mobile_number']
        city = request.POST['city']
        gender = request.POST['gender']
        dob = request.POST['dob']
        join_date = request.POST['join_date1']
        student_class = request.POST['class']
        school = request.POST['school']
        student = Student(
            name=name,
            email=email,
            age=age,
            phone=mobile_number,
            city=city,
            gender=gender,
            dob=convert_str_to_date(dob),
            join_date=convert_str_to_date(join_date),
            class_id=StudentClass.objects.get(pk=int(student_class)),
            school_id=School.objects.get(pk=int(school)),
        )
        student.save()
        return redirect('students')
    else:
        student_class = StudentClass.objects.all()
        schools = School.objects.all().order_by('name')
        data = {
            'student_class': student_class,
            'schools': schools,
        }
        return render(request, 'school/create_student.html', data)

@login_required
def students(request):
    students = Student.objects.all().order_by('id')
    students_under_18 = Student.objects.filter(age__lt=18)
    students_not_from_ahmedabad = Student.objects.exclude(city='ahmedabad')

    # not proper solution for group by
    # results = Student.objects.raw('SELECT * FROM myapp_members GROUP BY designation')
    # group by class student
    # query = Student.objects.all().query
    # query.group_by = ['class_id']
    # student_group_by_class = QuerySet(query=query, model=Student)

    student_class = StudentClass.objects.all()

    student_highest_skill = Student.objects.annotate(count_skill=Count('skil')).order_by('-count_skill')
    data = {
        'students': students,
        'students_under_18': students_under_18,
        'students_not_from_ahmedabad': students_not_from_ahmedabad,
        'student_class': student_class,
        'student_highest_skill': student_highest_skill,
    }
    return render(request, 'school/students-list.html', data)
