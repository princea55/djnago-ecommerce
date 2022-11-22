from django.urls import path
from . import views
from .middleware.main import BlockMobileMiddleware, auth_middleware

urlpatterns = [
    path('', views.index, name='index'),
    path('students', BlockMobileMiddleware(views.students), name='students'),
    path('create-student', auth_middleware(views.create_students), name='create-student'),
    path('create-teacher', views.create_teacher, name='create-teacher'),
    path('update-student/record/<int:id>', views.update_student_record, name='update-student-record'),
    path('update-student/<int:id>', views.update_student, name='update-student'),
    path('delete-student/<int:id>', views.delete_student, name='delete-student'),

    path('teachers-list', views.teachers_list, name='teachers-list'),
    path('update-teacher/<int:id>', views.update_teacher, name='update-teacher'),
    # path('update-teacher/<int:id>/record', views.update_teacher_record, name='update-teacher-record'),
]
