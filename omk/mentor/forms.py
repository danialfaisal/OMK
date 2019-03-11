from django import forms
from .models import Semester, Week, School, Student, Mentor, Meeting

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('semester_name',)

class WeekForm(forms.ModelForm):
   class Meta:
       model = Week
       fields = ('week_number', 'week_startdate',)

class SchoolForm(forms.ModelForm):
   class Meta:
       model = School
       fields = ('school_name',)

class StudentForm(forms.ModelForm):
   class Meta:
       model = Student
       fields = ('stud_id', 'stud_name', 'stud_dob', 'stud_gender', 'stud_address', 'stud_city', 'stud_state', 'stud_zipcode', 'stud_email', 'stud_phoneno', 'stud_image', 'stud_school',)

class MentorForm(forms.ModelForm):
   class Meta:
       model = Mentor
       fields = ('mentor_id', 'mentor_name', 'mentor_gender', 'mentor_address', 'mentor_city', 'mentor_state', 'mentor_zipcode', 'mentor_email', 'mentor_phoneno', 'mentor_image',)

class MeetingForm(forms.ModelForm):
   class Meta:
       model = Meeting
       fields = ('semester', 'week', 'mentor', 'stud_name', 'meeting_time', 'attendance', 'notes',)