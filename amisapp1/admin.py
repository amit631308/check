from django.contrib import admin
from .models import userType_table
from .models import patientBookAppointment
from .models import queryForm
from .models import doctor_detail,dawa_category,dawa_add_product,medicin,lab_profile,lab_report,lab_reply



# Register your models here.



admin.site.register(userType_table)
admin.site.register(patientBookAppointment)
admin.site.register(queryForm)
admin.site.register(doctor_detail)
admin.site.register(dawa_category)
admin.site.register(dawa_add_product)
admin.site.register(medicin)
admin.site.register(lab_profile)
admin.site.register(lab_report)
admin.site.register(lab_reply)