from django.shortcuts import render
from bilhetes.models import Bilhete


def index(request):

    todos_bilhetes = Bilhete.objects.all()

    context = {
        "nome_pagina": "Inicio da dashboard",
        'todos_bilhetes': todos_bilhetes,

    }
    return render(request, "index.html", context)

