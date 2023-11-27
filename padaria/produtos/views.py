from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from padaria.produtos.models import Produto, Pedido


def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', context={'produtos': produtos})


def fazer_pedido(request, produto_id: int):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'pedido.html', context={'produto': produto})


def sucesso(request):
    return render(request, 'sucesso.html')


def finalizar_pedido(request, produto_id: int):
    produto = get_object_or_404(Produto, id=produto_id)
    pedido = Pedido.objects.get_or_create(nome_comprador=request.POST.nome, endereco=request.POST.endereco)
    pedido.produtos.add(produto)

    return redirect('sdge')
