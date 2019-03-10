from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect





def home(request):
    return render(request, 'attendance/home.html', {'home': home})

def contactus(request):
    return render(request, 'attendance/contactus.html', {'contactus': contactus})

def faq(request):
    return render(request, 'attendance/faq.html', {'faq': faq})