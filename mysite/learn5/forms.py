# coding:utf-8
from django import forms

from learn5.models import Member,Material,Running,Running_Member,Running_Material

class AddForm(forms.Form):
    a = forms.IntegerField(label='鸡蛋')
    b = forms.IntegerField(label='面包')
    c = forms.IntegerField(label='馒头')
    r = forms.IntegerField(label='单号')
    MemberNameListO=Member.objects.all()#values('name')
    # MemberNameList=[];
    # for i in MemberNameListO:
    #     MemberNameList.append(i['name'])
    InMember=forms.ModelChoiceField(
        queryset = MemberNameListO,
        label=u"项目负责人",
        empty_label='None'
        )
    

