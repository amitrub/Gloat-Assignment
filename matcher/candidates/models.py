import json

from django.db import models
from skills.models import Skill


class Candidate(models.Model):
    """Candidate Model"""

    title = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
