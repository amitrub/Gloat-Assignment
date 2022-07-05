import json

from django.db import models


class Skill(models.Model):
    """Skill Model"""

    name = models.CharField(max_length=255)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
