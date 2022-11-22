# Generated by Django 4.1.3 on 2022-11-14 05:59

from django.db import migrations, models
import school.models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_subject_teacher_studentclass_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_code',
            field=models.CharField(default=school.models.next_by_code, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_code',
            field=models.CharField(default=school.models.next_by_code_teacher, editable=False, max_length=50, unique=True),
        ),
    ]
