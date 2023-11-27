from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('produto/<int:produto_id>/', views.fazer_pedido, name='pedido'),
    path('produto/finalizar/<int:produto_id>/', views.finalizar_pedido, name='finalizar'),
    path('produto/sucesso', views.sucesso, name='sucesso')
]
