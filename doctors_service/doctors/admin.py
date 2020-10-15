from django.contrib import admin

from .models import *


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "county",
        "specialization",
        "license_number",
    )

    class Meta:
        model = Doctor


admin.site.register(Doctor, DoctorAdmin)
