# Generated by Django 4.1.3 on 2022-11-14 03:42

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('teacher_code', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=60)),
                ('city', models.CharField(choices=[('ahmedabad', 'Ahmedabad'), ('surat', 'Surat'), ('rajkot', 'Rajkot')], max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=255)),
                ('dob', models.DateField()),
                ('join_date', models.DateField(blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('student_code', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=60)),
                ('city', models.CharField(choices=[('ahmedabad', 'Ahmedabad'), ('surat', 'Surat'), ('rajkot', 'Rajkot')], max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=255)),
                ('dob', models.DateField()),
                ('join_date', models.DateField(blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('section', models.CharField(blank=True, max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentclass')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
        ),
    ]
