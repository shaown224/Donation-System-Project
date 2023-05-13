from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


def Index(request):
    return HttpResponseRedirect(reverse('Donor_App:Donor_dashboard'))
