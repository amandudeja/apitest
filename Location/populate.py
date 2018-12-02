import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Location.settings')
import django
django.setup()


from myapp.models import Location
import csv


with open("IN.csv") as f:
	reader = csv.reader(f)
	for row in reader:
		created = Location.objects.get_or_create(
			key = row[0],
			place_name = row[1],
			admin_name = row[2],
			latitude = row[3],
			longitude = row[4],
			)

