from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

regex=r'[0-9]'

# Create your models here.
class Semester(models.Model):
    semester_name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.semester_name



class Week(models.Model):
    week_number = models.CharField(max_length=10, db_index=True)
    week_startdate = models.DateTimeField()


    def __str__(self):
        return self.week_number




class School(models.Model):
    school_name = models.CharField(max_length=50, db_index=True)


    def __str__(self):
        return self.school_name



class Student(models.Model):

    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    stud_id = models.CharField(max_length=50, unique=True, db_index=True)
    stud_name = models.CharField(max_length=20, blank=False)
    stud_dob = models.DateField()
    stud_gender = models.CharField(max_length=1, choices=gender_choices, default='M')
    stud_address = models.CharField(max_length=200)
    stud_city = models.CharField(max_length=50)
    stud_state = models.CharField(max_length=50)
    stud_zipcode = models.CharField(max_length=10)
    stud_email = models.EmailField(max_length=100)
    stud_phoneno = models.CharField(validators=[MinLengthValidator(10), RegexValidator(regex)], max_length=10)
    stud_image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    stud_school = models.ForeignKey(School, related_name='student_school', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stud_name)



class Mentor(models.Model):
    mentor_id = models.CharField(max_length=50, unique=True, db_index=True)
    mentor_name = models.CharField(max_length=20, blank=False)
    mentor_gender = models.CharField(max_length=10, null=True, help_text="Enter F or M")
    mentor_address = models.CharField(max_length=200)
    mentor_city = models.CharField(max_length=50)
    mentor_state = models.CharField(max_length=50)
    mentor_zipcode = models.CharField(max_length=10)
    mentor_email = models.EmailField(max_length=100)
    mentor_phoneno = models.CharField(validators=[MinLengthValidator(10), RegexValidator(regex)], max_length=10)
    mentor_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.mentor_name)



class Meeting(models.Model):

    attendance_choices = (
        ('P', 'Present'),
        ('A', 'Absent'),
        ('T', 'Tardy'),
    )

    semester = models.ForeignKey(Semester, related_name='semester', on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='weeknumber', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, related_name='mentorname', on_delete=models.CASCADE)
    stud_name = models.ForeignKey(Student,related_name='studentname', on_delete=models.CASCADE)
    meeting_time = models.TimeField(blank=False)
    attendance = models.CharField(max_length=1, choices=attendance_choices, default='P')
    notes= models.CharField(max_length=250,default='meeting notes')

    def __str__(self):
        return str(self.id)

    def create(self):
        self.attend_date = timezone.now()
        self.save()