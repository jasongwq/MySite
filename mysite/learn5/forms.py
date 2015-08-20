# coding:utf-8
from django import forms

from learn5.models import Member,Material,Running,Running_Member,Running_Material

class AddForm(forms.Form):
    a = forms.IntegerField(label='鸡蛋')
    b = forms.IntegerField(label='面包')
    c = forms.IntegerField(label='馒头')
    r = forms.IntegerField(label='单号')
    qs=Member.objects.values_list('name')
    InMember=forms.ModelChoiceField(queryset = qs, empty_label='None')

