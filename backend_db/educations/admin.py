from django.contrib import admin

# Register your models here.
from .models import School, Degree, DegreeView, UserProfile

admin.site.register(Degree)
admin.site.register(DegreeView)
admin.site.register(School)
admin.site.register(UserProfile)