from django.urls import path

from Organization_App import views

app_name = 'Organization_App'
urlpatterns = [
    path('', views.Organization_dashboard, name='Organization_home'),
    path('donationlist/', views.Donation_list, name='donation_list'),
    path('donationslist/<int:id>', views.Details_Donations, name='DetailsDonation')

]
