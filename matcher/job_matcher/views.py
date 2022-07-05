from django import views
from django.db.models import Count, Q
from django.http import HttpResponse
from rest_framework import viewsets, generics
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
    filter_backends = [CandidateFilterByJob]


class TryView(views.View):
    def get(self, request):
        # <view logic>
        job_id = 1
        job = models.Job.objects.get(pk=job_id)
        job_title = job.title
        job_skills = job.skills.all().values_list('id', flat=True)
        candidates = models.Candidate.objects.filter(title=job_title)
        candidates = candidates.annotate(num_skills=Count('skills', filter=Q(skills__id__in=job_skills))).order_by(
            '-num_skills').values()

        return HttpResponse(job_skills)
