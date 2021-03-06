from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name='inicio'),
    path('download-report/', views.generate_report, name='download-report'),
    path('download-tag/', views.generate_tags, name='download-tag'),
]