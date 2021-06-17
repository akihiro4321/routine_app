from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from target.form import SetGoalForm
from target.models import Goal


class IndexView(TemplateView):
    template_name = 'index.html'

class GoalCreateView(CreateView):
    model = Goal
    fields = ('goal',)
    template_name = 'set-goal.html'
    success_url = reverse_lazy('target:index')


