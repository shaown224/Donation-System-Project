from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_App.urls')),
    path('2/', include('Login_App.urls')),
    path('donor/', include('Donor_App.urls')),
    path('organization/', include('Organization_App.urls')),
    path('', views.Index, name='index')
]

urlpatterns += staticfiles_urlpatterns()
