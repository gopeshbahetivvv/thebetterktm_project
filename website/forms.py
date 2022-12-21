from socket import fromshare
from types import MemberDescriptorType
from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model= Problem
        fields = ('name', 'emailid', 'number', 'subject', 'problemtext', 'anonymity')