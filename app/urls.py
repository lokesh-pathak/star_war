from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view()),
    url(r'^search/$', views.Search.as_view(), name='search'),
    url(r'^add/$', views.AddData.as_view(), name='add'),
]
