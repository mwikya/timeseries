
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include,re_path
from django.contrib.auth.views import LogoutView
from .views import fit_curve

app_name = 'fit'
urlpatterns = [
	path('',fit_curve, name='fiting'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)