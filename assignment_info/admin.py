from django.contrib import admin

# Register your models here.
from .models import Course,Submissions,Cname,RegUsers
admin.site.register(Submissions)
admin.site.register(Course)
admin.site.register(Cname)
admin.site.register(RegUsers)
