from django.contrib import admin
from .models import Donor, Volunteer, DonationArea, Donation, Gallery

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact', 'address', 'userpic', 'regdate')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact', 'address', 'userpic', 'regdate')

@admin.register(DonationArea)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'areaname', 'description', 'creationdate')

@admin.register(Donation)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'volunteer', 'donationarea', 'donationname')
@admin.register(Gallery)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'donation', 'deliverypic', 'creationdate')
