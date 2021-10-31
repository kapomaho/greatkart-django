from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from greatkart.settings import MEDIA_ROOT
from . import views
from django.conf.urls.static import static
from django.conf import Settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('store/',include('store.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

