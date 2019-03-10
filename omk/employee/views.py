from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from mentor.models import Mentor, Week, Student, Meeting, timezone
from .forms import *
from django.contrib.auth.decorators import login_required

now= timezone.now()

@login_required
def employeehome(request):
    mentors = Mentor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'employee/employeehome.html',
                  {'mentors': mentors})

def employee_schedule(request, pk):
    mentor = get_object_or_404(Mentor, pk=pk)
    mentors = Mentor.objects.filter(created_date__lte=timezone.now())
    meetings = Meeting.objects.filter(mentor_id=pk)
    return render(request, 'employee/employee_schedule.html', {'mentors': mentors,
                                                'meetings': meetings,
                                                })

def update_attendance(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == "POST":
        # update
        form = AttendanceForm(request.POST, instance=meeting)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.save()
            meet = meeting.mentor_id
            meetings = Meeting.objects.filter(mentor_id=meet)
            mentors = Mentor.objects.filter(created_date__lte=timezone.now())
            return render(request, 'employee/employee_schedule.html', {'mentors': mentors,
                                                                        'meetings': meetings, })

    else:
        # edit
        form = AttendanceForm(instance=meeting)
    return render(request, 'employee/update_attendance.html', {'form': form})
