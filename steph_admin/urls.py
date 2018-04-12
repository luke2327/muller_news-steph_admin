from django.urls import path

from . import views
app_name = 'steph_admin'
urlpatterns = [
    path('players/', views.players, name='players'),
    path('followings/', views.followings, name='followings'),
]
