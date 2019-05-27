# -*- coding: utf-8 -*-
from django.db import models


class Mainframe(models.Model):
    name = models.CharField(max_length=50)
    ip = models.CharField(max_length=20)
    subarea = models.CharField(max_length=50)
    system = models.CharField(max_length=10, choices=(('Windows', 'Windows'), ('Mac', 'Max'), ('Linux', 'Linux')),
                              default='Windows')
    remark = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
