import re
import operator
from functools import reduce

from django.db.models import Count, Q, F, Value, CharField
from rest_framework import filters
from rest_framework.exceptions import NotFound
from django.template import loader

from job_matcher import models
from matcher.settings import BASE_DIR


def str_to_int(str1):
    try:
        return int(str1)
    except:
        return None


def get_title_match_str(title_match):
    default = 'full'
    if title_match and title_match.lower() == "partial":
        return title_match.lower()
    return default


class CandidateFilterByJob(filters.BaseFilterBackend):
    # template = 'rest_framework/filters/ordering.html'
    template = f'{BASE_DIR}/templates/candidate_filter_by_job.html'
    param_job = 'job_id'
    param_limit = 'limit_number'
    param_title_match = 'title_match'
    partial_title_match = "partial"
    full_title_match = "full"

    def filter_queryset(self, request, queryset, view):
        job_id_str = request.query_params.get(self.param_job)
        job_id = str_to_int(job_id_str)
        limit_number_str = request.query_params.get(self.param_limit)
        limit_number = str_to_int(limit_number_str)
        title_match = get_title_match_str(request.query_params.get(self.param_title_match))
        if job_id:
            try:
                job = models.Job.objects.get(pk=job_id)
            except models.Job.DoesNotExist:
                raise NotFound(detail="Job id not found")
            job_title = job.title
            job_skills = job.skills.all().values_list('id', flat=True)

            if not title_match == self.partial_title_match:
                queryset = queryset.filter(title=job_title)
                queryset = queryset.annotate(
                    num_skills=Count('skills', filter=Q(skills__id__in=job_skills))).order_by('-num_skills')

            # Bonus part
            else:
                job_title_list = list(map(lambda x: re.sub(r"[^a-zA-Z0-9]", "", x), job_title.split()))
                job_title_query_list = list(map(lambda x: Q(title__icontains=x), job_title_list))
                queryset = queryset.filter(reduce(operator.or_, job_title_query_list)).exclude(
                    title=job_title)
                queryset = queryset.annotate(
                    num_skills=Count('skills', filter=Q(skills__id__in=job_skills))).order_by('-num_skills')

        if limit_number:
            queryset = queryset[:limit_number]
        return queryset

    def get_template_context(self, request, queryset, view):
        options = []
        current_param_job = request.query_params.get(self.param_job)
        current_param_limit = request.query_params.get(self.param_limit)
        current_param_title_match = get_title_match_str(request.query_params.get(self.param_title_match))
        context = {
            'request': request,
            'current_param_job': current_param_job,
            'current_param_limit': current_param_limit,
            'current_param_title_match': current_param_title_match,
            'param_job': self.param_job,
            'param_limit': self.param_limit,
            'param_title_match': self.param_title_match,
            'partial_title_match': self.partial_title_match
        }
        jobs = models.Job.objects.all()
        for job in jobs:
            options.append((str(job.id), str(job)))
        context['options'] = options
        return context

    def to_html(self, request, queryset, view):
        template = loader.get_template(self.template)
        context = self.get_template_context(request, queryset, view)
        return template.render(context)
