from django.contrib import admin

#Register your models here.
from .models import Departments,Doctors,Booking


admin.site.register(Departments)
admin.site.register(Doctors)

class bookingAdmin(admin.ModelAdmin):
 list_display = ('p_name','p_phone','p_email','doc_name','booking_date','booked_on')
 list_filter = ('p_name','p_phone','doc_name','booking_date')
admin.site.register(Booking,bookingAdmin)


