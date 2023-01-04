from django.contrib import admin


from .models import User, Course, Profile, Schedule, Relationship, Comment




class CourseAdmin(admin.ModelAdmin):
    model = Course

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Course, CourseAdmin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Schedule)

admin.site.register(Relationship)

admin.site.register(Comment)
