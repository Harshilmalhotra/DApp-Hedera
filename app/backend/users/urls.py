# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path, re_path, include

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from . import views

app_name = "users"

urlpatterns = [
    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
	path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]