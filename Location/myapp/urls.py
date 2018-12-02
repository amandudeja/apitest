from django.urls import path
from myapp import views


app_name = 'myapp'
urlpatterns = [

	path('',views.find,name = 'find'),
	path('add',views.add,name = 'add'),
	path('getplace',views.get,name = 'get'),



]