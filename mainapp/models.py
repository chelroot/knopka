#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Knopka(models.Model):
    name = models.CharField(max_length=32)
