from rest_framework import serializers

from job_matcher import models


class SkillSerializer(serializers.ModelSerializer):
    """Serializer Skill"""

    class Meta:
        model = models.Skill
        fields = ('id', 'name')


class CandidateSerializer(serializers.ModelSerializer):
    """Serializer Candidate"""

    # skills = SkillSerializer(many=True)
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = models.Candidate
        fields = ('id', 'title', 'skills')
