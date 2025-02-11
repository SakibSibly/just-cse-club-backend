from django.contrib import admin
from .models import Role, OTP, CustomUser, Department, Faculty, Tag, Blog, Comment, Event, Notice, Feedback, Donation


admin.site.register(Role)
admin.site.register(OTP)
admin.site.register(CustomUser)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(Feedback)
admin.site.register(Donation)
