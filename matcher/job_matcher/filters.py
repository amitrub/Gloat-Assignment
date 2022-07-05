from django.db.models import Count, Q
from rest_framework import filters
from rest_framework.exceptions import NotFound
from django.template import loader

from job_matcher import models
from matcher.settings import BASE_DIR


class CandidateFilterByJob(filters.BaseFilterBackend):
    template = 'rest_framework/filters/ordering.html'

    def filter_queryset(self, request, queryset, view):
        job_id = request.query_params.get('job_id')
        try:
            job_id = int(job_id)
        except:
            job_id = None
        if job_id:
            try:
                job = models.Job.objects.get(pk=job_id)
            except models.Job.DoesNotExist:
                raise NotFound(detail="Job id not found")
            job_title = job.title
            job_skills = job.skills.all().values_list('id', flat=True)
            candidates = models.Candidate.objects.filter(title=job_title)
            candidates = candidates.annotate(num_skills=Count('skills', filter=Q(skills__id__in=job_skills))).order_by(
                '-num_skills')
            return candidates

        return queryset

    def get_template_context(self, request, queryset, view):
        options = []
        context = {
            'request': request,
            'param': 'job_id',
        }
        jobs = models.Job.objects.all()
        for job in jobs:
            options.append((job.id, str(job)))
        context['options'] = options
        return context

    def to_html(self, request, queryset, view):
        template = loader.get_template(self.template)
        with open(f'{BASE_DIR}\candidate_filter_by_job.html', 'r') as file:
            data = file.read()
        template.template.source = data
        context = self.get_template_context(request, queryset, view)
        return template.render(context)




class FilterByJobID(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        job_id = request.query_params.get('job_id')
        try:
            job_id = int(job_id)
        except:
            job_id = None
        if job_id:
            try:
                job = models.Job.objects.get(pk=job_id)
            except models.Job.DoesNotExist:
                raise NotFound(detail="Job id not found")
            job_title = job.title
            job_skills = job.skills.all().values_list('id', flat=True)
            candidates = models.Candidate.objects.filter(title=job_title)
            candidates = candidates.annotate(num_skills=Count('skills', filter=Q(skills__id__in=job_skills))).order_by(
                '-num_skills')
            return candidates

        return queryset