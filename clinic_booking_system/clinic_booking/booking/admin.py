from django.contrib import admin

from .models import Patient,PatientHistory,Payment_status,Fee,Service,Threapy,Treatment,Doctorrefer,Report,Month_Summary


admin.site.register(Patient)
admin.site.register(PatientHistory)
admin.site.register(Payment_status)
admin.site.register(Fee)
admin.site.register(Service)
admin.site.register(Threapy)
admin.site.register(Treatment)
admin.site.register(Doctorrefer)
admin.site.register(Report)
admin.site.register(Month_Summary)

# Register your models here.
