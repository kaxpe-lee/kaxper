from django.urls import path
from plantillas.views import saludo, inicio, some_view

from . import views

app_name = 'plantillas'

urlpatterns = [
    path('pdf', some_view),
    path('', inicio),

    path('<int:id>/', views.detail, name='detail'),

    path('<int:id>/results/', views.results, name='results'),

    path('<int:id>/vote/', views.vote, name='vote'),

    path('saludo/', saludo),
]
