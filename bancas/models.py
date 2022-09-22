
from django.db import models


class Banca(models.Model):


    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.PROTECT
    )
    
    nome_banca = models.CharField(
        verbose_name='Nome da Banca: ',
        max_length=100,
    )

    valor_inicial_banca = models.IntegerField(
        verbose_name='Valor inicial da banca',
    )

    data_inicio_banca = models.DateTimeField(
        verbose_name='Data inicio banca',
        auto_now_add=True,
    )

    

    class Meta:
        verbose_name="Banca"
        verbose_name_plural="Bancas"
        db_table="banca"
    
    def __str__(self):
        return self.nome_banca