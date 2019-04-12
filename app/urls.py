from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.HomeView),
    url(r'^film/$', views.Film.as_view(), name='film'),
    url(r'^planet/$', views.Planet.as_view(), name='planet'),
    url(r'^add/$', views.AddData.as_view(), name='add'),
]
