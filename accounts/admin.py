from django.contrib import admin
from .models import Doctor,Patient,Appointment,Schedule,Administrator,SystemUser

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Administrator)
admin.site.register(Appointment)
admin.site.register(Schedule)
admin.site.register(SystemUser)