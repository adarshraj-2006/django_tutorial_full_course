from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('notes/', views.NoteList.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name='notes.detail'),
    path('notes/<int:pk>/edit/', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete/', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('notes/new/', views.NotesCreateView.as_view(), name='notes.new'),
    path('login',views.LoginInterfaceView.as_view(),name='login'),
    path('logout',views.LogoutInterfaceView.as_view(),name='logout'),
]