from rest_framework import viewsets

from job_matcher import serializers, models


class SkillViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating skills"""
    serializer_class = serializers.SkillSerializer
    queryset = models.Skill.objects.all()


class CandidateViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating candidates"""
    serializer_class = serializers.CandidateSerializer
    queryset = models.Candidate.objects.all()
