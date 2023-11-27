from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField()


class Pedido(models.Model):
    nome_comprador = models.CharField(max_length=50)
    endereco = models.TextField()
    produtos = models.ManyToManyField(Produto)
    data = models.DateTimeField(auto_now=True)
