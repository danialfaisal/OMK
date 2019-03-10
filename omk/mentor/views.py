from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required




now = timezone.now()
@login_required
def mentorhome(request):
   return render(request, 'mentor/mentorhome.html',
                 {'mentor': mentorhome})


# SEMESTER
def semester_list(request):
    semesters = Semester.objects.filter()
    return render(request, 'mentor/semester_list.html',
                 {'semesters': semesters})

def semester_new(request):
   if request.method == "POST":
       form = SemesterForm(request.POST)
       if form.is_valid():
           semester = form.save(commit=False)
           semester.created_date = timezone.now()
           semester.save()
           semesters = Semester.objects.filter()
           return render(request, 'mentor/semester_list.html',
                         {'semesters': semesters})
   else:
       form = SemesterForm()
       # print("Else")
   return render(request, 'mentor/semester_new.html', {'form': form})

def semester_edit(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if request.method == "POST":
        # update
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            semester = form.save(commit=False)
            semester.updated_date = timezone.now()
            semester.save()
            semesters = Semester.objects.filter()
            return render(request, 'mentor/semester_list.html',
                          {'semesters': semesters})
    else:
        # edit
        form = SemesterForm(instance=semester)
    return render(request, 'mentor/semester_edit.html', {'form': form})

def semester_delete(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    semester.delete()
    return redirect('mentor:semester_list')





# WEEK
def week_list(request):
    weeks = Week.objects.filter()
    return render(request, 'mentor/week_list.html',
                 {'weeks': weeks})

def week_new(request):
   if request.method == "POST":
       form = WeekForm(request.POST)
       if form.is_valid():
           week = form.save(commit=False)
           week.created_date = timezone.now()
           week.save()
           weeks = Week.objects.filter()
           return render(request, 'mentor/week_list.html',
                         {'weeks': weeks})
   else:
       form = WeekForm()
       # print("Else")
   return render(request, 'mentor/week_new.html', {'form': form})

def week_edit(request, pk):
    week = get_object_or_404(Week, pk=pk)
    if request.method == "POST":
        # update
        form = WeekForm(request.POST, instance=week)
        if form.is_valid():
            week = form.save(commit=False)
            week.updated_date = timezone.now()
            week.save()
            weeks = Week.objects.filter()
            return render(request, 'mentor/week_list.html',
                          {'weeks': weeks})
    else:
        # edit
        form = WeekForm(instance=week)
    return render(request, 'mentor/week_edit.html', {'form': form})

def week_delete(request, pk):
    week = get_object_or_404(Week, pk=pk)
    week.delete()
    return redirect('mentor:week_list')





# SCHOOL
def school_list(request):
    schools = School.objects.filter()
    return render(request, 'mentor/school_list.html',
                 {'schools': schools})

def school_new(request):
   if request.method == "POST":
       form = SchoolForm(request.POST)
       if form.is_valid():
           school = form.save(commit=False)
           school.created_date = timezone.now()
           school.save()
           schools = School.objects.filter()
           return render(request, 'mentor/school_list.html',
                         {'schools': schools})
   else:
       form = SchoolForm()
       # print("Else")
   return render(request, 'mentor/school_new.html', {'form': form})

def school_edit(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == "POST":
        # update
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            school = form.save(commit=False)
            school.updated_date = timezone.now()
            school.save()
            schools = School.objects.filter()
            return render(request, 'mentor/school_list.html',
                          {'schools': schools})
    else:
        # edit
        form = SchoolForm(instance=school)
    return render(request, 'mentor/school_edit.html', {'form': form})

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    school.delete()
    return redirect('mentor:school_list')





# MEETING
def meeting_list(request):
    meetings = Meeting.objects.filter()
    return render(request, 'mentor/meeting_list.html',
                 {'meetings': meetings})

def meeting_new(request):
   if request.method == "POST":
       form = MeetingForm(request.POST)
       if form.is_valid():
           meeting = form.save(commit=False)
           meeting.created_date = timezone.now()
           meeting.save()
           meetings = Meeting.objects.filter()
           return render(request, 'mentor/meeting_list.html',
                         {'meetings': meetings})
   else:
       form = MeetingForm()
       # print("Else")
   return render(request, 'mentor/meeting_new.html', {'form': form})

def meeting_edit(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    if request.method == "POST":
        # update
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.updated_date = timezone.now()
            meeting.save()
            meetings = Meeting.objects.filter()
            return render(request, 'mentor/meeting_list.html',
                          {'meetings': meetings})
    else:
        # edit
        form = MeetingForm(instance=meeting)
    return render(request, 'mentor/meeting_edit.html', {'form': form})

def meeting_delete(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    meeting.delete()
    return redirect('mentor:meeting_list')





# STUDENT
def student_list(request):
    students = Student.objects.filter(created_date__lte=timezone.now())
    return render(request, 'mentor/student_list.html',
                 {'students': students})

def student_new(request):
   if request.method == "POST":
       form = StudentForm(request.POST)
       if form.is_valid():
           student = form.save(commit=False)
           student.created_date = timezone.now()
           student.save()
           students = Student.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mentor/student_list.html',
                         {'students': students})
   else:
       form = StudentForm()
       # print("Else")
   return render(request, 'mentor/student_new.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        # update
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.updated_date = timezone.now()
            student.save()
            students = Student.objects.filter(created_date__lte=timezone.now())
            return render(request, 'mentor/student_list.html',
                          {'students': students})
    else:
        # edit
        form = StudentForm(instance=student)
    return render(request, 'mentor/student_edit.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('mentor:student_list')





# MENTOR
def mentor_list(request):
    mentors = Mentor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'mentor/mentor_list.html',
                 {'mentors': mentors})

def mentor_new(request):
   if request.method == "POST":
       form = MentorForm(request.POST)
       if form.is_valid():
           mentor = form.save(commit=False)
           mentor.created_date = timezone.now()
           mentor.save()
           mentors = Mentor.objects.filter(created_date__lte=timezone.now())
           return render(request, 'mentor/mentor_list.html',
                         {'mentors': mentors})
   else:
       form = MentorForm()
       # print("Else")
   return render(request, 'mentor/mentor_new.html', {'form': form})

def mentor_edit(request, pk):
    mentor = get_object_or_404(Mentor, pk=pk)
    if request.method == "POST":
        # update
        form = MentorForm(request.POST, instance=mentor)
        if form.is_valid():
            mentor = form.save(commit=False)
            mentor.updated_date = timezone.now()
            mentor.save()
            mentors = Mentor.objects.filter(created_date__lte=timezone.now())
            return render(request, 'mentor/mentor_list.html',
                          {'mentors': mentors})
    else:
        # edit
        form = MentorForm(instance=mentor)
    return render(request, 'mentor/mentor_edit.html', {'form': form})

def mentor_delete(request, pk):
    mentor = get_object_or_404(Mentor, pk=pk)
    mentor.delete()
    return redirect('mentor:mentor_list')
