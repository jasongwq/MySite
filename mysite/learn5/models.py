#coding:utf-8
from django.db import models

# Create your models here.


# class Itemname(models.Model):#成员
# 	name   = models.CharField(max_length=4,blank=False)#名称
# 	remark = models.TextField(blank=True)#备注

class Member(models.Model):#成员 ok
	name   = models.CharField(max_length=4,blank=False)#名称
	funds  = models.FloatField(default=0.0)#资金
	remark = models.TextField(blank=True)#备注

class Material(models.Model):#物品 ok
	name   = models.CharField(max_length=4,blank=False)#名称
	number = models.IntegerField(blank=False,default=0)#数量
	units  = models.CharField(default='单位',max_length=4,blank=True)#单位
	total  = models.FloatField(default=0)#总金额
	remark = models.TextField(blank=True)#备注

class Running(models.Model):#流水 ok
	# runningId = models.CharField(max_length=30,blank=False)#流水号
	itemtime  = models.DateField(blank=False,auto_now_add=True)#时间
	itemname  = models.CharField(max_length=30)#流水名称
	remark    = models.TextField(blank=True)#备注

class Running_Member(models.Model):#流水 用户对应表 ok
	running = models.ManyToManyField(Running)##流水名称
	member = models.ManyToManyField(Member)#
	remark = models.TextField(blank=True)#备注

class Running_Material(models.Model):#流水 物品对应表 ok
	runnings = models.ManyToManyField(Running)##流水名称
	materials = models.ManyToManyField(Material)#
	remark = models.TextField(blank=True)#备注
