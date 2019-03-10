from django.contrib import admin
from .models import Semester, Week, School, Student, Mentor, Meeting




class SemesterList(admin.ModelAdmin):
    list_display = ['semester_name']
    list_filter = ['semester_name']
    ordering = ['semester_name']


class WeekList(admin.ModelAdmin):
    list_display = ('week_number', 'week_startdate')
    search_fields = ('week_number', 'week_startdate')

class SchoolList(admin.ModelAdmin):
    list_display = ['school_name']
    list_filter = ['school_name']
    ordering = ['school_name']

class StudentList(admin.ModelAdmin):
    list_display = ('stud_id', 'stud_name','stud_school', 'stud_email')
    search_fields =  ('stud_id', 'stud_name','stud_school', 'stud_email')

class  MentorList(admin.ModelAdmin):
    list_display = ('mentor_id','mentor_name','mentor_email')

class  MeetingList(admin.ModelAdmin):
    list_display = ('semester','week','mentor', 'stud_name', 'meeting_time', 'present')


admin.site.register(Semester,SemesterList )
admin.site.register(Week,WeekList)
admin.site.register(School, SchoolList)
admin.site.register(Student, StudentList)
admin.site.register(Mentor, MentorList)
admin.site.register(Meeting, MeetingList)
