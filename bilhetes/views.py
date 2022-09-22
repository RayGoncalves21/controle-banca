from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from bilhetes.models import Bilhete
from bilhetes.forms import BilheteForm, AtualizaBilheteForm
from django.utils import timezone

def registrar_bilhete(request):

    form = BilheteForm()


    if request.method == "POST":
        form = BilheteForm(request.POST)

        if form.is_valid():
            bilhete = form.save(commit=False)


            bilhete.banca_apostada = request.user.banca
            bilhete.save()


            messages.success(
                request,
                "Bilhete registrado com sucesso"
            )

            return redirect("index")

    

    context = {
        "nome_pagina": "registrar_bilhete",
        "form": form
    }

    return render(request, "registrar_bilhete.html", context)

def informacoes_bilhete(request, id):

    bilhete = get_object_or_404(
        Bilhete,
        id=id
    )

    form = AtualizaBilheteForm()
    

    if request.method == "POST":
        form = AtualizaBilheteForm(
            request.POST,
            instance=bilhete
        )

        if form.is_valid():
            bilhete = form.save(commit=False)

            bilhete.status = "AGUARDANDO"
            
            bilhete.save()

            messages.success(
                request,
                "Bilhete atualizado com sucesso"
            )

            return redirect("index")
    
    context = {
        "nome_pagina": "Informações Bilhetes",
        "bilhete": bilhete,
        "form": form
    }
    
    return render(request, "informacoes_bilhete.html", context)