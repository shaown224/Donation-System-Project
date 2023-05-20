from django.urls import path

from Donor_App import views


app_name = 'Donor_App'
urlpatterns = [
    path('', views.Donor_dashboard, name='Donor_dashboard'),
    path('createform/', views.Donation_Create.as_view(), name='create_donation'),
]
