from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from job_matcher import models
from job_matcher.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    """Serializer Skill"""

    class Meta:
        model = models.Skill
        fields = ('id', 'name')

class SkillSerializer2(PrimaryKeyRelatedField, serializers.ModelSerializer):
    """Serializer Skill"""

    class Meta:
        model = models.Skill
        fields = ('id', 'name')


class CandidateSerializer(serializers.ModelSerializer):
    """Serializer Candidate"""

    skills = SkillSerializer2(many=True, queryset=Skill.objects.all())
    # skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = models.Candidate
        fields = ('id', 'title', 'skills')
