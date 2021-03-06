from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import VolOppForm
from .models import VolOpp

def home(request):
    return render(request, 'SimpactApp/index.html')

def businessLogin(request):
    return render(request, 'SimpactApp/businesslogin.html')

def npoLogin(request):
    return render(request, 'SimpactApp/npologin.html')

def volLogin(request):
    return render(request, 'SimpactApp/volunteerlogin.html')
    
def volDashboard(request):
    return render(request, 'SimpactApp/vdash.html')

def npoDash(request):
    return render(request, 'Users/dashboardbase.html')

def npoDashboard(request):
    return render(request, 'SimpactApp/npodash.html')

def busPerks(request):
    return render(request, 'SimpactApp/allperks.html')
    
def busNewPerks(request):
    return render(request, 'SimpactApp/newperks.html')
    
def busPromote(request):
    return render(request, 'SimpactApp/promote.html')

def simpactAbout(request):
    return HttpResponse('<h1> this is the about page <h1>')


def testPath(request):
    return HttpResponse('<h1> hello testing <h1>')


def voloppdescription(request):
    return render(request, 'SimpactApp/voloppdescription.html')


#Add testing
def add_volopp(request):
    submitted = False
    if request.method == 'POST':
        form = VolOppForm(request.POST, request.FILES)
        if form.is_valid():
            form.vol_photo = request.FILES['vol_photo']
            form.save()
#            return HttpResponseRedirect('add_volopp/?submitted=True')
#            return HttpResponseRedirect('/?submitted=True')
            return render(request, 'SimpactApp/voloppsubmitted.html')
    else:
        form = VolOppForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
        'SimpactApp/add_volopp.html',
        {'form': form, 'submitted': submitted}
        )


# Showing All Volunteer Opportunities in Database
def all_volopps(request):
    volopp_list = VolOpp.objects.all()
    return render(request,
        'SimpactApp/volopplisting.html',
        {'volopp_list': volopp_list}
    )


#testing 
def all_events(request):
    event_list = VolOpp.objects.all()
    return render(request,
        'SimpactApp/volopp_list.html',
        {'event_list': event_list}
    )



# Create your views here.
