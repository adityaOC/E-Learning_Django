from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.StudentProfile)
admin.site.register(models.TeacherProfile)
admin.site.register(models.Course)
admin.site.register(models.Video)
admin.site.register(models.CourseRatings)
