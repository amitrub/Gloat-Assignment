from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from job_matcher import models


class SkillSerializer(serializers.ModelSerializer):
    """Serializer Skill"""

    class Meta:
        model = models.Skill
        fields = ('id', 'name')


class SkillSerializer2(PrimaryKeyRelatedField, serializers.ModelSerializer):
    """Serializer Skill"""

    class Meta:
        model = models.Skill
        fields = ('name',)


class SkillCandidateSerializer(serializers.ModelSerializer):
    """Serializer Skill Candidate"""

    class Meta:
        model = models.Skill
        fields = ('name',)


class CandidateSerializer(serializers.ModelSerializer):
    """Serializer Candidate"""
    # skills = SkillSerializer2(many=True, queryset=Skill.objects.all())
    # skills = SkillCandidateSerializer(read_only=True, many=True)
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = models.Candidate
        fields = ('id', 'title', 'skills')
