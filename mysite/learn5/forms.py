# coding:utf-8
from django import forms

from learn5.models import Member,Material,Running,Running_Member,Running_Material

class AddForm(forms.Form):
    a = forms.IntegerField(label='鸡蛋')
    b = forms.IntegerField(label='面包')
    c = forms.IntegerField(label='馒头')
    r = forms.IntegerField(label='单号')
    InMember=forms.ModelChoiceField(
        queryset = Member.objects.all(),
        label=u"项目负责人",
        empty_label='None'
        )
    subject_type = forms.ModelMultipleChoiceField(
        label=u'学科', 
        queryset=Member.objects.all(), 
        required=True,
        widget=forms.CheckboxSelectMultiple
        )
    # 多选(checkbox)