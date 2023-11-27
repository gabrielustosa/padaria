from django.contrib import admin

from padaria.produtos.models import Produto, Pedido

admin.site.register(Produto)
admin.site.register(Pedido)
