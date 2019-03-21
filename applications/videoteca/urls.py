from django.urls import include, path, re_path
from . import views

app_name = "videoteca_app"

urlpatterns = [
    #en el '' path habia un 'listamoves/'
    path('bboys/', views.ListaBboys.as_view(), name="lista-bboys"),
    path('movimientos-bboy/<pk>/por-bboy/', views.ListaPowerBboys.as_view(), name="lista-movimientos"),
    path('bboy/add/', views.AddBboy.as_view(), name="bboy-add"),
    path('', views.ListaMovimientos.as_view(),name="lista"),


]