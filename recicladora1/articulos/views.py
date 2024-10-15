# Create your views here.
from django.shortcuts import render, redirect
from .forms import ArticulosForm
from .models import Articulos
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def registrar_articulo(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.usuario = request.user
            articulo.save()
            return redirect('imprimir_recibo', articulo_id=articulo.id)
    else:
        form = ArticulosForm()
    return render(request, 'registrar_articulo.html', {'form': form})

@login_required
def imprimir_recibo(request, articulo_id):
    articulo = Articulos.objects.get(id=articulo_id)
    total_a_pagar = articulo.cantidad * articulo.valor
    return render(request, 'imprimir_recibo.html', {'articulo': articulo, 'total_a_pagar': total_a_pagar})

