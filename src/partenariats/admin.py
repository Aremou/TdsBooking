from django.contrib import admin

from partenariats.models import Demandes

# Register your models here.


@admin.register(Demandes)
class DemandesAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "phone",
        "email",
        "etablishment_type",
        "status",

    )
    list_editable = ('status',)
