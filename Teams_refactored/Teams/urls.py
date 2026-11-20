from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('teams/<slug:team_slug>/', views.team_detail, name='team_detail'),
]
