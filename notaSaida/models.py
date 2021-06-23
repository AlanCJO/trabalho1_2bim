from django.db import models
from produto.models import Produtos


class NotaSaida(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.PROTECT)
    numero_nota = models.IntegerField('Número da nota')
    quantidade = models.IntegerField('Quantidade', default=0)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=8)

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Nota de Saida'
        verbose_name_plural = "Notas de Saida"
        ordering = ['-produto']

    def __str__(self):
        return self.produto.produto
