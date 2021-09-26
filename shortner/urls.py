from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('go/<str:pk>', views.go, name='go'),
    path('<str:link>', views.tothelink, name='tothelink'),
]
