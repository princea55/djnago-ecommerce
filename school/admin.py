from django.contrib import admin
from .models import School, Subject, StudentClass, Student, Teacher, Skill


class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "email", 'city', 'created_at', 'updated_at')
    list_display_links = ("name",)
    search_fields = ("name", "email")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ("name", "subject_id",)
    list_display_links = ("name",)
    search_fields = ("name", "subject_id")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_code", "name", "email", 'age', 'city', 'created_at', 'updated_at')
    list_display_links = ("student_code", "name",)
    search_fields = ("student_code", "name", "email")


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_code", "name", "email", 'city', 'created_at', 'updated_at')
    list_display_links = ("teacher_code", "name",)
    search_fields = ("teacher_code", "name", "email")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)


admin.site.register(School, SchoolAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Skill, SkillAdmin)
