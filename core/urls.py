from django.urls import path

from .views import IndexView, CreateProdutoView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/', CreateProdutoView.as_view(), name='cadastrar_produto')
]
