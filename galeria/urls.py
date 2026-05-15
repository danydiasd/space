from django.urls import path
from galeria.views import index, imagem, buscar, surpreenda_me

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('surpreenda-me/', surpreenda_me, name='surpreenda-me'),
]