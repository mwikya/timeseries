from django.contrib import admin
from django.urls import path,include
from fit.views import home

urlpatterns = [
	path('',home,name='home'),
    path('admin/', admin.site.urls),
    path('fit/',include('fit.urls')),
]
