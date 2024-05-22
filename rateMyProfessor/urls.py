from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings






urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
