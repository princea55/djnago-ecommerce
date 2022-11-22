from django_cron import CronJobBase, Schedule
from .models import Student
from datetime import datetime


class StudentAgeCalculationCronJob(CronJobBase):
    RUN_EVERY_MINS = 120  # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'school.age_calculation_cron_job'  # a unique code

    def do(self):
        students = Student.objects.all()
        for student in students:
            if student.dob:
                student.age = datetime.today().year - student.dob.year
                student.save()
                print(f"{student.name} age is {student.age}.")
            else:
                student.age = 0
                print("Student date not found.")
