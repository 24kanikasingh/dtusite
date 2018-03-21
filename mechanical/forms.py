from django import forms

ATTENDANCE_CHOICES = [('yes','Yes'), ('no','No')]
SYLLABUS_CHOICES = [('yes','Yes'), ('no','No')]
ON_TIME_CHOICES = [('a','Always'), ('s','Sometimes'),('n','Never')]
TEACH_AID_CHOICES = [('a','Always'), ('s','Sometimes'),('n','Never')]
AVAIL_CHOICES = [('yes','Yes'), ('no','No')]



class RateForm(forms.Form):
    att = forms.ChoiceField(choices=ATTENDANCE_CHOICES, widget=forms.RadioSelect(),label='Takes Attendance?')
    syll=forms.ChoiceField(choices=SYLLABUS_CHOICES, widget=forms.RadioSelect(),label='Completes syllabus on time?')
    time=forms.ChoiceField(choices=ON_TIME_CHOICES, widget=forms.RadioSelect(),label='Does professor come on time?')
    teach_aids=forms.ChoiceField(choices=TEACH_AID_CHOICES, widget=forms.RadioSelect(),label='Does professor uses teaching aids?')
    avail=forms.ChoiceField(choices=AVAIL_CHOICES, widget=forms.RadioSelect(),label='Is professor available after class ?')
