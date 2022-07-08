from rest_framework import viewsets, generics
from job_matcher import serializers, models
from job_matcher.filters import CandidateFilterByJob


class SkillViewSet(viewsets.ModelViewSet):
    """Handle creating, reading and updating skills"""
    serializer_class = serializers.SkillSerializer
    queryset = models.Skill.objects.all()


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    filter_backends = (CandidateFilterByJob,)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer


# ----------------- Multi Choice Example -----------------

class CandidateMultiChoiceViewSet(generics.ListCreateAPIView):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateMultiChoiceSerializer
