from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
# Create your views here.
import datetime
import sqlite3




def current_datetime(request):
 now = datetime.datetime.now()
 html = "<html><body>It is now %s.</body></html>" % now
 return HttpResponse(html)


def hours_ahead(request, offset):
 offset = int(offset)
 dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
 html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
 return HttpResponse(html)


class IOT(TemplateView):
	template_name = "myapp/header_first.html"
	'''conn = sqlite3.connect('sensor.db')
	print "Opened database successfully";

	cursor = conn.execute("SELECT *  from sensor.water_quality")
	for row in cursor:
	   print "ID = ", row[0]
	   print "NAME = ", row[1]
	   print "ADDRESS = ", row[2]
	   print "ADDRESS = ", row[3]
	   print "SALARY = ", row[4], "\n"

	print "Operation done successfully";
	conn.close()'''
	def get_context_data(self, **kwargs):
		context= super(IOT, self).get_context_data(**kwargs)
		context = {'name':["Sarvani", "pranavi"]}
		return context

#class DateShowView(TemplateView):
	#template_name = "myapp/date.html"
	#def get_context_data(self, **kwargs):
		#context= super(DateShowView, self).get_context_data(**kwargs)
		#context = {'name':["Sarvani", "pranavi"]}
		#return context

def index(request,name,value):

	temp_sen_data = Sensor()
	temp_sen_data.Sensor_name = name
	temp_sen_data.Sensor_value = value
	temp_sen_data.save()



def index2(request,group,name,value):
	temp_sen_data = Sensorgroup2()

	temp_sen_data.Sensorgroup2_name = name
	temp_sen_data.Sensorgroup2_value = value
	temp_sen_data.save()


def allsensors(request):
    sensors = Sensor.objects.all()
    sensors=sensors.reverse()[:2]
    print sensors
    context  = {
        "sensors":sensors,
    }
    return render(request,"myapp/sensor_data.html",context)

def sensors(request):
    sensors = Sensor.objects.all()
    print sensors
    context  = {
        "sensors":sensors,
    }
    return render(request,"myapp/sensors.html",context)


def previous(request):
    sensors = Sensor.objects.all()
    print sensors
    context  = {
        "sensors":sensors,
    }
    return render(request,"myapp/previous_data.html",context)
