#coding:utf-8
from django.db import models

class Sms(models.Model):
	name = models.CharField(max_length=64)
	phone = models.CharField(max_length=64)
	content = models.TextField()
	def _get_phone(self):
	        a = "%s"%self.phone
        	return  a[:6]
	phone_hide = property(_get_phone)
