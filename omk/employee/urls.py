from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'employee'
urlpatterns = [
    path('', views.employeehome, name='employeehome'),
    path('employee/<int:pk>/schedule/', views.employee_schedule, name='employee_schedule'),
    path('update/<int:pk>/attendance/', views.update_attendance, name='update_attendance'),

]