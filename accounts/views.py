from django.shortcuts import render,redirect
from .models import Doctor,Patient,Appointment,Administrator,Schedule,SystemUser
from .forms import AdminForm,PatientForm,AppointmentForm,ScheduleForm,DoctorForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):

    return render(request,'index.html',{})


def loginAdmin(request,pk):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            typeUser = SystemUser.objects.filter(user=user)
            
            login(request,user)
            if(pk==1):
                admin = typeUser.filter(is_admin=True)
                if(admin):
                   return redirect('adminHome')
                else:
                    messages.success(request,"cannot redirect. Make sure you are admin")
            elif (pk==2):
                admin = typeUser.filter(is_doctor=True)
                if(admin):
                    return redirect('doctorHome')
                else:
                    messages.success(request,"cannot redirect. Make sure you are a doctor")
            elif (pk==3):
                admin = typeUser.filter(is_patient=True)
                if(admin):
                    return redirect('patientHome')
                    
                else:
                    messages.success(request,"cannot redirect. Make sure you are a patient")
            
           
        else:
            messages.error(request,"Login details are incorrect")
    return render(request,'login.html')

def adminHome(request):
    if request.method=="POST":
        loadedForm=ScheduleForm(request.POST)
        if loadedForm.is_valid():
            loadedForm.save()

    lform = ScheduleForm()
    schedules = Schedule.objects.all()
    context={
        'scheduleForm':lform,
        'schedules':schedules
    }

    return render(request,'adminHome.html',context)

def patientHome(request):
    p=get_object_or_404(Patient,id=1)
        
    schedules = Schedule.objects.filter(booked=False)
    app = Appointment.objects.filter(patient=p)
    context={
        
        'schedules':schedules,
        'appoint':app
    }
    print(request.user)

    return render(request,'adminPatient.html',context)

def bookAppointment(request,pk):
    schedule = get_object_or_404(Schedule,id=pk)

    patient = Patient.objects.get(id=1)
    s=Appointment(doctor=schedule.doctor,patient=patient,date_time=schedule.date,confirmed=False);
    s.save()
    schedule.booked=True
    schedule.save()
    return redirect('patientHome')

def doctorHome(request):
    
    doc = Doctor.objects.get(id=1)     
    schedules = Appointment.objects.filter(doctor=doc)
    pending = schedules.filter(confirmed=False)
    con = schedules.filter(confirmed=True)
    context={
        
        'schedules':pending,
        'confirmed':con
    }
    print(request.user)

    return render(request,'doctorHome.html',context)

def confirmAppointment(request,pk):
    appoint = get_object_or_404(Appointment,id=pk)
    appoint.confirmed=True
    appoint.save()
    return redirect('doctorHome')