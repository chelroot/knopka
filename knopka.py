#!/usr/bin/python3
# -*- coding: utf-8 -*-
#import os

import os, sys

ddir='/home/vova/rasb/knopka/'
sys.path.append(ddir)

#b=os.getcwd()
#print(b)

from mainapp.models import *
knopka = Knopka()
knopka.name  = 'Testo3'
knopka.save()
#a=Organization.objects.filter(region='Пермь')
#print(a)
#q=Organization.objects.filter()
#print(q)