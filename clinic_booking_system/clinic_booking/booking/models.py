from django.db import models

class Patient(models.Model):
    patient_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.BigIntegerField()
    email=models.CharField(max_length=100,null=True,blank=True)
    alternate_number=models.CharField(null=True,blank=True)
    is_refered=models.BooleanField(default=False)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()

    def __str__(self):
        return self.patient_name

class PatientHistory(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=100)
    prescription=models.FileField(upload_to="pdf/",null=True)
    treatment_detail=models.TextField(null=True)
    duration=models.IntegerField()
    is_threapytaken=models.BooleanField(default=False)
    first_time=models.BooleanField(default=True)

    def __str__(self):
        return f'{self.patient_name}'

class Doctorrefer(models.Model):
    refer_doctor=models.CharField(max_length=100)

    def __str__(self):
        return self.refer_doctor

class Threapydetail(models.Model):
    sugar_beforebreakfast=models.IntegerField()
    sugar_afterbreakfast=models.IntegerField()
    doctor_suggestion=models.TextField()
    
    def __str__(self):
        return f'{self.sugar_beforebreakfast}-{self.sugar_afterbreakfast}'
    
class Diagnose(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE)
    height=models.IntegerField()
    weight=models.IntegerField()
    bp=models.IntegerField()
    diabetic=models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name

class Payment_status(models.Model):
    payment_status=models.CharField(max_length=100)

    def __str__(self):
        return self.payment_status

class Fee(models.Model):
    patient_name=models.ForeignKey(Patient,on_delete=models.CASCADE)
    consultation_charge=models.IntegerField()
    threapy_charge=models.IntegerField()
    other_charges=models.IntegerField()
    tax=models.IntegerField(default=50)
    date=models.DateField()
    time=models.TimeField()
    payment_status=models.ForeignKey(Payment_status,on_delete=models.CASCADE)
    qr_code=models.FileField(upload_to="image/")
    total_amount=models.IntegerField(default=0)


    def __str__(self):
        return f'{self.patient_name}-{self.payment_status}'
    
class Service(models.Model):
    service=models.CharField(max_length=100)


    def __str__(self):
        return self.service
    
class Threapy(models.Model):
    threapy=models.CharField(max_length=100)


    def __str__(self):
        return self.threapy

class Treatment(models.Model):
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    threapy=models.ForeignKey(Threapy,on_delete=models.CASCADE)
    treatment_detail=models.TextField(max_length=100)
    follow_up=models.DateField()

    def __str__(self):
        return f'{self.service}-{self.threapy}-{self.follow_up}'

class Report(models.Model):
    fee=models.ForeignKey(Fee,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.patient}-{self.fee}'
    
class Month_Summary(models.Model):
    fee=models.ForeignKey(Fee,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.patient}-{self.fee}'

   

   

# Create your models here.
