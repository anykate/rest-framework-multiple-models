from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.showmultiplemodels, name='show_multiple_models'),
    path('api/showmultiplemodels/', views.api_showmultiplemodels,
         name='api_show_multiple_models'
         ),
]
