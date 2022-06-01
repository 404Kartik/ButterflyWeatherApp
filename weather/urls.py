from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('delete/', views.delete_everything, name='delete_everything'),
    path('ips/', views.ip_loc, name='ip_loc'),

]

urlpatterns += staticfiles_urlpatterns()