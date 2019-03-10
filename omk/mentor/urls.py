from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'mentor'
urlpatterns = [
    path('', views.mentorhome, name='mentorhome'),

    # SEMESTER
    path('semester_list/', views.semester_list, name='semester_list'),
    path('semester/create/', views.semester_new, name='semester_new'),
    path('semester/<int:pk>/edit/', views.semester_edit, name='semester_edit'),
    path('semester/<int:pk>/delete/', views.semester_delete, name='semester_delete'),

    # WEEK
    path('week_list/', views.week_list, name='week_list'),
    path('week/create/', views.week_new, name='week_new'),
    path('week/<int:pk>/edit/', views.week_edit, name='week_edit'),
    path('week/<int:pk>/delete/', views.week_delete, name='week_delete'),

    # SCHOOL
    path('school_list/', views.school_list, name='school_list'),
    path('school/create/', views.school_new, name='school_new'),
    path('school/<int:pk>/edit/', views.school_edit, name='school_edit'),
    path('school/<int:pk>/delete/', views.school_delete, name='school_delete'),

    # STUDENT
    path('student_list/', views.student_list, name='student_list'),
    path('student/create/', views.student_new, name='student_new'),
    path('student/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # MENTOR
    path('mentor_list/', views.mentor_list, name='mentor_list'),
    path('mentor/create/', views.mentor_new, name='mentor_new'),
    path('mentor/<int:pk>/edit/', views.mentor_edit, name='mentor_edit'),
    path('mentor/<int:pk>/delete/', views.mentor_delete, name='mentor_delete'),

    # MEETING
    path('meeting_list/', views.meeting_list, name='meeting_list'),
    path('meeting/create/', views.meeting_new, name='meeting_new'),
    path('meeting/<int:pk>/edit/', views.meeting_edit, name='meeting_edit'),
    path('meeting/<int:pk>/delete/', views.meeting_delete, name='meeting_delete'),

]

urlpatterns = format_suffix_patterns(urlpatterns)