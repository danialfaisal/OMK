from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'attendance'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),

    path('contactus', views.contactus, name='contactus'),
    path('faq', views.faq, name='faq'),

]
