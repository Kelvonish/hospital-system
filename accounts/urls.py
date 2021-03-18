

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/<int:pk>/',views.loginAdmin, name='adminLogin'),
    path('home/admin',views.adminHome, name='adminHome'),
    path('home/patient',views.patientHome, name='patientHome'),
    path('home/doctor',views.doctorHome, name='doctorHome'),
    path('bookAppointment/<int:pk>', views.bookAppointment,name='book'),
    path('confirm/appointment/<int:pk>', views.confirmAppointment,name='confirm')
    
]