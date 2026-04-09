from django.contrib import admin
from .models import Booking, Profile


# 📅 BOOKING ADMIN
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'student_class',
        'subject',
        'area',
        'status',
        'assigned_teacher',
        'created_at'
    )

    list_filter = ('status', 'area')
    search_fields = ('name', 'subject')


# 👤 PROFILE ADMIN (optional but useful)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')