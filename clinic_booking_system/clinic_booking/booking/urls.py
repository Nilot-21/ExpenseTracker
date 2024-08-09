from django.urls import path
from . import views
urlpatterns=[
    path("",views.patientregis,name="patient"),
    path("refe/",views.patiref,name="refer"),
    path("history/",views.history,name="history"),
    path("threapy/",views.threapy,name="threapy"),
    path("diagnose",views.diagnose,name="diagnose"),
    path("fee/",views.feevalidation,name="fee"),
    path("report/",views.report,name="report"),
    path("summary/",views.summary,name="summary")
]