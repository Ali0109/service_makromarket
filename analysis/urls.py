from django.urls import re_path
from . import views

app_name = 'analysis'

urlpatterns = [
    # DEVICE
    re_path(
        r'^device/users/count/?$',
        views.AnalysisAPIView.as_view({'get': 'device_users_count'}),
        name='device_users_count',
    ),
    re_path(
        r'^device/users/count/(?P<year>\d+)/(?P<month>\d+)/?$',
        views.AnalysisAPIView.as_view({'get': 'device_users_month_count'}),
        name='device_users_month_count',
    ),
    re_path(
        r'^device/users/count/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/?$',
        views.AnalysisAPIView.as_view({'get': 'device_users_day_count'}),
        name='device_users_day_count',
    ),
    # CARD
    re_path(
        r'^card/users/count/?$',
        views.AnalysisAPIView.as_view({'get': 'card_users_count'}),
        name='card_users_count',
    ),
    # USER
    re_path(
        r'^users/count/?$',
        views.AnalysisAPIView.as_view({'get': 'users_count'}),
        name='users_count',
    ),
    re_path(
        r"^users/count/(?P<year>\d+)/(?P<month>\d+)/?$",
        views.AnalysisAPIView.as_view({'get': 'users_month_count'}),
        name='users_month_count',
    ),
    re_path(
        r"^users/count/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/?$",
        views.AnalysisAPIView.as_view({'get': 'users_day_count'}),
        name='users_day_count',
    ),
    # ---
    re_path(
        r'^users/named/count/?$',
        views.AnalysisAPIView.as_view({'get': 'users_named_count'}),
        name='users_named_count',
    ),
    re_path(
        r'^users/birthday/count/?$',
        views.AnalysisAPIView.as_view({'get': 'users_birthday_count'}),
        name='users_birthday_count',
    )
]
