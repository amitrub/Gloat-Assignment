from django import views
from django.db.models import Count, Q
from django.http import HttpResponse
from rest_framework import viewsets, generics, filters
from job_matcher import serializers, models
from job_matcher.filters import CandidateFilterByJob


class SkillViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating skills"""
    serializer_class = serializers.SkillSerializer
    queryset = models.Skill.objects.all()


class CandidateViewSet(generics.ListCreateAPIView):
    """Handle creating, reading and updating candidates"""
    serializer_class = serializers.CandidateSerializer
    queryset = models.Candidate.objects.all()


class CandidateListView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    filter_backends = (CandidateFilterByJob, )

