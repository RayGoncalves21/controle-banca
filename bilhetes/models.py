from django.db import models


class Bilhete(models.Model):

    STATUS_BILHETE = [
        ("AGUARDANDO", "Aguardando"),
        ("GREEN", "Green"),
        ("RED", "Red")

    ]

    status = models.CharField(
        verbose_name='status',
        max_length=11,
        choices = STATUS_BILHETE,
        default="AGUARDANDO"
    )

    time_casa = models.CharField(
        verbose_name="Time jogando em casa",
        max_length=194,
        blank=True,
        null=True

    )

    time_fora = models.CharField(
        verbose_name="Time jogando fora",
        max_length=194,
        blank=True,
        null=True

    )

    valor_aposta = models.IntegerField(
        verbose_name='Valor apostado R$',
   )

    cotacao = models.FloatField(
        verbose_name="Cotação"
   )

    banca_apostada = models.ForeignKey(
        'bancas.Banca',
        verbose_name='Banca que aconteceu a aposta',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        
    )

    horario_aposta = models.DateTimeField(
        verbose_name='Horario aposta',
        auto_now_add=True
    )

    def get_jogo(self):
        time_home = str(self.time_casa)
        time_away = str(self.time_fora)

        jogo_formatado = f'{time_home} x {time_away}'

        return jogo_formatado
    
    

    def get_valor_aposta(self):
        valor = self.valor_aposta

        valor_formatado = f'R$ {valor}'

        return valor_formatado

    def valor_ganho(self):
        valor = self.valor_aposta
        cotacao = self.cotacao

        ganho = valor * cotacao
        ganho_total = "{:.2f}".format(ganho)
        ganho_formatado = f"R$ {ganho_total}"


        return ganho_formatado

         

    class Meta:
        verbose_name ='Bilhete'
        verbose_name_plural ='Bilhetes',
        db_table ='bilhete'

    def __str__(self):
        return self.time_casa