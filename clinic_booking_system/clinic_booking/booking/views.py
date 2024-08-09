from django.shortcuts import render,redirect
from .form import (PatientForm,DoctorreferForm,
                   PatientHistoryForm,ThreapydetailForm,DiagnoseForm,FeeForm)

from .models import Fee,Patient,Report,Month_Summary
from datetime import date,datetime
from django.db.models import Q
from django.utils.dateparse import parse_date
import calendar
from django.db.models import Count,Sum
from django.db.models.functions import ExtractMonth,ExtractYear
def patientregis(request):
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            is_refer=form.cleaned_data['is_refered']
           
            print(is_refer)
            if is_refer:
                print("hello")
                return redirect('refer')
           
    else:
        form=PatientForm()
    return render(request,"home.html",{"form":form})
    
def patiref(request):
    if request.method=='POST':
        form=DoctorreferForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=DoctorreferForm()
    return render(request,"refer.html",{"form":form})

def history(request):
    if request.method=="POST":
        form=PatientHistoryForm(request.POST,request.FILES)
        if form.is_valid(): 
            doctor_name=form.cleaned_data["doctor_name"]
            print(doctor_name)
            threapy=form.cleaned_data["is_threapytaken"]
            if threapy:
                return redirect("threapy")
            
    else:
        form=PatientHistoryForm()
    return render(request,"history.html",{"form":form})
# Create your views here.

def threapy(request):
    if request.method=='POST':
        form=ThreapydetailForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=form=ThreapydetailForm()
    return render(request,"threapy.html",{"form":form})

def diagnose(request):
    if request.method=="POST":
        form=DiagnoseForm(request.POST)
        if form.is_valid():
            form.save()
            is_diabetic=form.cleaned_data["diabetic"]
            
            if is_diabetic:
                return redirect('threapy')
    else:
        form=DiagnoseForm()
    return render(request,"diagnose.html",{"form":form})

def feevalidation(request):
    total=0
    if request.method=="POST":
        form=FeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()              
    else:
        form=FeeForm()
    return render(request,"fee.html",{"form":form,"total":total})


def report(request):
    det=Report.objects.all()
    patientdet=Report.objects.all()
    total_amount=0
    if request.method=='POST':
        patientname=request.POST.get("patient_name")
        from_date=request.POST.get("from")
        print(patientname)
        start=parse_date(from_date)
        to_date=request.POST.get("to")
        end=parse_date(to_date)
        print(type(end))
        print(end)
        if patientname=="all":
            det=Report.objects.all()
        else:
            det=det.filter(Q(patient__appointment_date__range=(start,end))|Q(patient__patient_name=patientname))

        total_fee=Report.objects.select_related('fee')

        for total in total_fee:
            total_amount=total_amount+total.fee.total_amount
        
        print(total_amount)
        # if(patientname=="all"):
        #     det=Report.objects.all()
        # else:
        # det=det.filter(patient__patient_name=patientname)
        # print(patientname)
        # from_date=request.POST.get("from")
        # start=datetime.strptime(from_date,'%Y-%m-%d').date()
        # print(type(start))
        # to_date=request.POST.get("to")
        # end=datetime.strptime(to_date,'%Y-%m-%d').date()
        # det=det.filter(patient__appointment_date__range=(start,end)) 
        return render(request,"report.html",{"detail":det,"name":patientdet,"total":total_amount})  
    return render(request,"report.html",{"detail":det,"name":patientdet,"total":total_amount})
    
        # if from_date and to_date:
        #     det_date=Report.objects.filter(patient__appointment_date__range=(start,end))
       

        # det=Report.objects.filter(Q(patient__appointment_date__range=(start,end))| Q(patient__patient_name=patientname))
        
     
    #     if patientname=="all":
    #         det=Report.objects.all()
    #         return render(request,"report.html",{"detail":det})
    #     else:
    #         # det=Report.objects.filter(patient__patient_name=patientname) 
    #         det=Report.objects.filter(patient__appointment_date__range=(start,end))
    #         return render(request,"report.html",{"detail":det})
    # else:
    #     detail=Report.objects.all()
    # return render(request,"report.html",{"detail":detail})

def summary(request):
    months=[]
    year=[]
    queryset=[]
    queryset_value=[]
    # total_length=0
    # summ=Month_Summary.objects.all()
    total_charge=0
    count=0
    selecte_month=0
    summ=Month_Summary.objects.all()
    for i in range(1,13):
            months.append(calendar.month_name[i])
    for ye in range(2011,(datetime.now().year+10)):
            year.append(ye)
    if request.method=="POST":
        selected_month=request.POST.get("month_dropdown")
        selected_year=request.POST.get("year_dropdown")
        if selected_month=="All" or selected_year=="All":   
            queryset=summ.annotate(month=ExtractMonth('patient__appointment_date')).values('month').annotate(count=Count('id'),sum=Sum('fee__total_amount')).order_by('month')                               
            print(queryset)
            for result in queryset:
                queryset_value.append({"count":result['count'],"total_charge":result['sum'],"selecte_month":calendar.month_name[result['month']],"isAudited":"yes"})
                print(queryset_value)
            # return render(request,"summary.html",{"years":year,"month":months,"queryset":queryset_value})
        else:
            print('selective')
            selecte_month=datetime.strptime(selected_month, '%B').month
            queryset=summ.filter(patient__appointment_date__month=selecte_month,
                                              patient__appointment_date__year=selected_year)
            print(queryset)
            count=queryset.count()
            total_charges_month=queryset.aggregate(total_charges_month=Sum('fee__total_amount'))
            total_charge=total_charges_month["total_charges_month"]
            print(count,total_charge)
            queryset_value.append({"count":count,"total_charge":total_charge,"selecte_month":selected_month,"isAudited":"yes"})
        return render(request,"summary.html",{"month":months,"years":year,"queryset":queryset_value})
    return render(request,"summary.html",{"years":year,"month":months,"queryset":queryset_value})
        
        #month_number = datetime.strptime(month_name, '%B').month

        