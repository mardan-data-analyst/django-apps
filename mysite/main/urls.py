from django.urls import path
from main import views


urlpatterns = [
path("<int:id>", views.index, name='index'),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.get_name, name="get_name"),
path("view/", views.view, name="view"),
]

