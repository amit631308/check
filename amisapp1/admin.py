from django.contrib import admin
from .models import userType_table
from .models import patientBookAppointment
from .models import queryForm


# Register your models here.



admin.site.register(userType_table)
admin.site.register(patientBookAppointment)
admin.site.register(queryForm)