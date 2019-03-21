from django.urls import include, path, re_path
from . import views

app_name = "home_app"

urlpatterns = [
    path('index/', views.IndexView.as_view(),name="index"),
    #path('movimientos/', views.ListaMovimientos.as_view(),name="lista"),

]