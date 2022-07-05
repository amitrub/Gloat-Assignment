from django.contrib import admin

from job_matcher import models

admin.site.register(models.Skill)
admin.site.register(models.Candidate)
admin.site.register(models.Job)
