import json

from django.db import models

class Skill(models.Model):
    """Skill Model"""

    name = models.CharField(max_length=255)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return self.name

class Candidate(models.Model):
    """Candidate Model"""

    title = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill,  blank=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    def __str__(self):
        return f'{self.id}.{self.title}'

class Job(models.Model):
    """Job Model"""

    title = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill, blank=True)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return f'{self.id}.{self.title}'
