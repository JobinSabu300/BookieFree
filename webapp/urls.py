from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('fiction', views.fiction, name='fiction'),
    path('non_fiction', views.non_fiction, name='non_fiction'),
    path('search',views.search,name='search'),
    path('download',views.download,name='download')
]