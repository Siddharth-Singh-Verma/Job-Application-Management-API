from django.contrib import admin
from .models import Applicant, Job, Application

admin.site.register(Applicant)
admin.site.register(Job)
admin.site.register(Application)
