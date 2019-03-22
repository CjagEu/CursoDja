from django.shortcuts import render

from .models import Bboy, Powermove

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,


)

# Create your views here.
class ListaBboys(ListView):
    template_name = "videoteca/lista-bboys.html"
    model = Bboy
    context_object_name = "listabboys"

class ListaPowerBboys(ListView):
    #Vista para listar movimientos por bboy
    template_name = 'videoteca/lista-moves.html'
    context_object_name = "movimientos"

    def get_queryset(self):
        id = self.kwargs['pk']
        lista = Powermove.objects.filter(
            bboy=id
        )
        return lista

class AddBboy(CreateView):
    template_name = 'videoteca/add-bboy.html'
    model = Bboy
    fields = ['name', 'nacionalidad']
    success_url = '/'


class ListaMovimientos(ListView):
    template_name = "videoteca/lista.html"
    context_object_name = "listamovimientos"

    def get_queryset(self):
        #id = self.kwargs['pk']
        lista = Powermove.objects.all()
        return lista

class ListaPowermoves(ListView):
    template_name = "videoteca/lista-powermoves.html"
    context_object_name = "listapowermoves"

    def get_queryset(self):
        lista = Powermove.objects.all()
        return lista
