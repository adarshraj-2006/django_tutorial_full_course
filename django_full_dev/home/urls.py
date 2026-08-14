from django.urls import path
from . import views

urlpatterns=[
    path('home',views.HomeView.as_view()),
    path('authorize',views.AuthorizeView.as_view),
]