from django.shortcuts import render
from jobsapp.models import HydJobs,BangaloreJobs,PuneJobs
# Create your views here.

def homepage_view(request):
    return render(request,'jobsapp/index.html')

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'jobsapp/hydjobs.html',context=my_dict)
