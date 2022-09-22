from django.contrib import admin
from django.urls import path
from usuarios.views import index
from bilhetes.views import registrar_bilhete, informacoes_bilhete

urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        "",
        index,
        name="index",
    ),

    path(
        "registrar-bilhete/",
        registrar_bilhete,
        name="registrar_bilhete",
    ),
    path(
        "bilhetes/<int:id>",
        informacoes_bilhete,
        name="informacoes_bilhete",
    )
]


