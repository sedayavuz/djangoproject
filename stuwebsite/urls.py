from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.management_view, name='post_list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
