from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("", views.gautam, name="gautam"),
  path("contact/", views.contact, name="contact"), 
    path("signout/", views.signout, name="signout"),
    path("spotify/",views.spotify_search,name="spotify"),
    path("login/", views.login,name="login"),
    path("homepage/", views.homepage,name="homepage"),
    path("index/", views.index, name="index"),
    path("anciya/", views.anciya, name="anciya"),


]
