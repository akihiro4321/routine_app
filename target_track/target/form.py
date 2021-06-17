from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy

from target.models import Goal


class SetGoalForm(forms.ModelForm):
    class Meta:
        models = Goal
        fields = ('goal',)