from django.shortcuts import render,redirect
from myapp.models import Location
from geopy.geocoders import Nominatim
from math import *

# Create your views here.
def index(request):
	locations = Location.objects.all()
	return render(request,'index.html',{'locations':locations})


def find(request):

	if request.method == "POST":
		lat1 = request.POST['latitude']
		lon1 = request.POST['longitude']
		rad  = request.POST['radius']
		print(type(lat1),type(lon1))
		# data = Location.objects.get(latitude=lat,longitude=lon)
		# print(data)
		locations = Location.objects.all()
		arr = []
		for location in locations:
			R = 6373.0
			try:
				lat2 = radians(location.latitude)
				lon2 = radians(location.longitude)

				dlon = lon2 - radians(float(lon1))
				print(type(dlon))
				dlat = lat2 - radians(float(lat1))
				print(type(dlat))
				try:
					a = sin(dlat / 2)**2 +cos(radians(float(lat1)))*cos(lat2)*sin(dlon/2)**2
					c = 2 * atan2(sqrt(a), sqrt(1-a))
					distance = R*c
				except Exception as e2:
					print(e2)

				if distance<=int(rad):
					arr.append(str(location.place_name)+
						" is at distance "
						+str(distance)
						+"km "
						+"--> Pincode is "
						+str(location.key))
				else:
					continue
			except Exception as e:
				print(e)
				print(location.key)
		print(arr)


		return render(request,'myapp/find.html',{'data':arr})

	return render(request,'myapp/find.html')


def add(request):
	if request.method == "POST":
		pin 	= "IN/"+str(request.POST['pincode'])
		place 	= request.POST['place'].capitalize()
		admin 	= request.POST['admin'].capitalize()
		lat 	= float(request.POST['latitude'])
		lon 	= float(request.POST['longitude'])

		print(pin)
		print(place)
		print(admin)
		print(lat)
		print(lon)

		location = Location.objects.get_or_create(key=pin,place_name=place,admin_name=admin,latitude=lat,longitude=lon)
		print(location)




	return render(request,'myapp/add.html')

def get(request):

	if request.method == "POST":
		lat = request.POST['latitude']
		lon = request.POST['longitude']
		loc ='"'+str(lat)+","+str(lon)+'"'
		try:
			geolocator = Nominatim(user_agent ='myapp')
			location = geolocator.reverse(loc)
			a = location.address
			a = a.split(',')
			return render(request,'myapp/get_place.html',{'data':a})
		except Exception as e:
			return render(request,'myapp/get_place.html',{'errors':'Invalid Coordinates'})


	return render(request,'myapp/get_place.html')
