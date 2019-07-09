from django.shortcuts import render
from django.http import HttpResponse
from . import job_data_test
from utility import helper
# Create your views here.

def home(request):
	return render(request, 'index.html', {'jobs': job_data_test.jobs})


def apply(request):
	return render(request, 'apply.html', {'message': 'Thank you for applying', 'jobs': job_data_test.jobs})

def parser(request):
	specific_job_raw = helper.trailing_slash(request.path)
	specific_job = specific_job_raw.split('/')[-1]
	for job in job_data_test.jobs:
		if job['url'] == specific_job:
			temp_var = job
			break
		else:
			continue

	return render(request, 'apply.html', {'job': temp_var})