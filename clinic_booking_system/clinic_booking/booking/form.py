from django import forms
from .models import Patient,Doctorrefer,PatientHistory,Threapydetail,Diagnose,Fee

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
        widgets={
            "appointment_time":forms.TimeInput(attrs={'type':'time'}),
            "appointment_date":forms.DateInput(attrs={'type':'date'})
        }

class DoctorreferForm(forms.ModelForm):
    class Meta:
        model=Doctorrefer
        fields='__all__'

class PatientHistoryForm(forms.ModelForm):
    class Meta:
        model=PatientHistory
        fields='__all__'

class ThreapydetailForm(forms.ModelForm):
    class Meta:
        model=Threapydetail
        fields="__all__"

class DiagnoseForm(forms.ModelForm):
    class Meta:
        model=Diagnose
        fields="__all__"

class FeeForm(forms.ModelForm):
    class Meta:
        model=Fee
        fields="__all__"
        widgets={
            "date":forms.TimeInput(attrs={'type':'date'}),
            "time":forms.TimeInput(attrs={'type':'time'})
        }