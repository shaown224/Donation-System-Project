from django.shortcuts import render

# Create your views here.


def Donor_dashboard(request):
    return render(request, 'Donor_App/Donor_Dashboard.html', context={})
