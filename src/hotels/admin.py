from xml.dom.pulldom import parseString
from django.contrib import admin

# Register your models here.
from hotels.models import CategoryEquipment, Category, Chambre, Equipment, Hotel, Image_Chambre, Image_Hotel, Payement, Reservation


class ImageHotel(admin.StackedInline):
    model = Image_Hotel


class ImageChambre(admin.StackedInline):
    model = Image_Chambre


# class Equipment(admin.StackedInline):
#     model = Equipment


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ville",
        "email",
        "tel_1",

    )
    search_fields = ('name', 'ville')

    inlines = [ImageHotel]

    class Meta:
        model = Hotel


@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "hotel",
        "number",
        "overnight",
        "capacity",
        "category",
        "is_delete",

    )

    search_fields = ('number', 'hotel__name', 'category__name')

    list_editable = ('overnight', 'is_delete',)

    inlines = [ImageChambre]

    class Meta:
        model = Chambre


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "chambre",
        "check_in",
        "check_out",
        "amount",
        "status",
        "add_at",
    )


@admin.register(Payement)
class PayementAdmin(admin.ModelAdmin):
    list_display = (
        "reservation",
        "payment_method",
        "add_at",
    )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "icon",
        "description",
        "hotel",
        "category",
        "is_admin",
        "token",
        "created_at",
        "updated_at",
    )
    # inlines = [Equipment]
    # class Meta:
    #     model = Equipment


@admin.register(CategoryEquipment)
class CategoryEquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "token",
        "created_at",
        "updated_at",
    )
    class Meta:
        model = CategoryEquipment

