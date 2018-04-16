from django.urls import path

from . import views
app_name = 'steph_admin'
urlpatterns = [
    path('players/', views.players, name='players'),
    path('followings/', views.followings, name='followings'),
    path('news_relation/', views.news_relation, name='news_relation'),
    path('vods_relation/', views.vods_relation, name="vods_relation")
]
