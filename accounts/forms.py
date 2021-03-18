from django import forms
from .models import Doctor,Patient,Appointment,Schedule,Administrator

class AdminForm(forms.ModelForm):

    class Meta: 
        model = Administrator 
        fields = "__all__"
        widgets = {
            'username':forms.TextInput(attrs={'type':'text','class':'form-control '}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control'}),
            
        }
class DoctorForm(forms.ModelForm):

    class Meta: 
        model = Doctor 
        fields = "__all__"
        widgets = {
            'username':forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control'}),
            
        }

class PatientForm(forms.ModelForm):

    class Meta: 
        model = Patient 
        fields = "__all__"
        widgets = {
            'username':forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'password':forms.TextInput(attrs={'type':'password','class':'form-control'}),
            
            
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"
        widgets = {
            
            'doctor':forms.Select(attrs={'class':'form-control'}),
            'date':forms.DateTimeInput(attrs={'type': 'datetime-local','class':'form-control'}),
            
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"
        widgets = {   
            'doctor':forms.Select(attrs={'class':'form-control'}),
            'patient':forms.Select(attrs={'class':'form-control'}),
            'date_time':forms.DateTimeInput(attrs={'type': 'date','class':'form-control'}),            
        }
