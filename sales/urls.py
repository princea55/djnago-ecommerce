from django.urls import path
from . import views


urlpatterns = [
    path('blog-list', views.BlogListView.as_view(), name='blog-list'),
    path('create-blog', views.BlogCreateView.as_view(), name='create-blog'),
    path('detail-blog/<int:id>', views.BlogDetailView.as_view(), name='detail-view-blog'),
    path('update-blog/<int:id>', views.BlogUpdateView.as_view(), name='update-blog'),
    path('delete-blog/<int:id>', views.BlogDeleteView.as_view(), name='delete-blog'),
    # path('update-student/record/<int:id>', views.update_student_record, name='update-student-record'),
    # path('update-student/<int:id>', views.update_student, name='update-student'),

    # path("delete/<int:pk>/", StudentDeleteView.as_view(), name="student-delete"),
    # path('teachers-list', views.teachers_list, name='teachers-list'),
    # path('update-teacher/<int:id>', views.update_teacher, name='update-teacher'),
    # path('update-teacher/<int:id>/record', views.update_teacher_record, name='update-teacher-record'),
]
