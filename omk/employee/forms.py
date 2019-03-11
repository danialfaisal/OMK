from django import forms
from mentor.models import Meeting


class AttendanceForm(forms.ModelForm):
   class Meta:
       model = Meeting
       fields = ('attendance', 'notes',)