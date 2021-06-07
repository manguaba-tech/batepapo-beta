from django.contrib import admin
from app.educa.models import Course, Subscription


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'student']

admin.site.register(Course, CourseAdmin)
admin.site.register(Subscription, SubscriptionAdmin)