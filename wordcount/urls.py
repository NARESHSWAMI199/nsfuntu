from django.urls import path
from . import view
urlpatterns = [ 
    path("", view.homepage, name = "home"),
    path("count/",view.counts ,name ="count"),
    path("aboutme/",view.about_me ,name = "aboutme"),
]
