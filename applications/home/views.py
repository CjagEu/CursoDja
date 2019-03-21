from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,

)

# Create your views here.
class IndexView(TemplateView):
    template_name = "home/index.html"

"""
class ListaMovimientos(ListView):
    template_name = "home/lista.html"
    queryset = ['Flare', 'Windmill','Swipe', 'Airflare']
    context_object_name = "listamovimientos"
"""