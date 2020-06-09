from django.conf.urls import url
from projects import views

app_name = 'projects'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^projects',views.projects,name='projects'),
    url(r'^contact',views.contact,name='contact'),
]
