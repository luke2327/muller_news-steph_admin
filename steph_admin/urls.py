from django.urls import path

from . import views
app_name = 'steph_admin'
urlpatterns = [
    path('players/', views.players, name='players'),
    path('followings/', views.followings, name='followings'),
    path('news_relation/', views.news_relation, name='news_relation'),
    path('vods_relation/', views.vods_relation, name="vods_relation"),
    path('lineup/', views.lineup, name="lineup"),
    path('one_value_change/', views.one_value_change, name="one_value_change"),
    path('push_send/', views.push_send, name="push_send"),
    path('best11/', views.best11, name="best11"),
]
