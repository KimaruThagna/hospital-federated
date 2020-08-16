from django.contrib import admin
from .models import Diagnosis


# Register your models here.
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("diagnosis", )

    class Meta:
        model = Diagnosis


admin.site.register(Diagnosis, DiagnosisAdmin)

# Register your models here.
