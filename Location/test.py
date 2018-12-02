import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Location.settings')
import django
django.setup()
from math import *

from myapp.models import Location



# location  =Location.objects.all()[10126:10276]

# for i in location:
# 	print(i.place_name)
# 	print(i.latitude)

import csv


with open("IN.csv") as f:
	reader = csv.reader(f)
	for row in list(reader)[10126:10276]:
		print(row)
