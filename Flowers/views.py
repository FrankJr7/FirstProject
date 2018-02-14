import datetime
from django.shortcuts import render

def index(request):
	myDate = datetime.datetime.now()		
	return render(request, 'Index.html', {'fecha_actual': myDate})
