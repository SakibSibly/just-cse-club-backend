from django.contrib import admin
from .models import Role, OTP, CustomUser, Department, Faculty, Blog, Comment, Event, Notice


admin.site.register(Role)
admin.site.register(OTP)
admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Event)
admin.site.register(Notice)
