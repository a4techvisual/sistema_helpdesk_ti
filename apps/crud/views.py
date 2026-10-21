from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Chamado
from .forms import ChamadoForm


def _resumo():
    """Totais exibidos nos cards do painel."""
    todos = Chamado.objects.all()
    return {
        'total': todos.count(),
        'abertos': todos.filter(status='aberto').count(),
        'andamento': todos.filter(status__in=['andamento', 'aguardando']).count(),
        'resolvidos': todos.filter(status='resolvido').count(),
        'criticos': todos.filter(prioridade='critica').exclude(status='resolvido').count(),
    }


# Create your views here.
@login_required
def index(request):
    chamados = Chamado.objects.all()
    status = request.GET.get('status', '')
    if status:
        chamados = chamados.filter(status=status)
    return render(request, "index.html", {
        'chamados':chamados,
        'resumo':_resumo(),
        'status_atual':status,
        'status_opcoes':Chamado.STATUS,
    })


@login_required
def novo_chamado(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            chamado = form.save()
            return redirect('novo_chamado_sucesso', codigo_chamado=chamado.codigo_chamado)
    else:
        form = ChamadoForm()
    return render(request, "novo-chamado.html",{
        'form':form,
    })


@login_required
def novo_chamado_sucesso(request, codigo_chamado):
    chamado = get_object_or_404(Chamado, codigo_chamado=codigo_chamado)
    return render(request, "novo-chamado-sucesso.html", {'chamado':chamado})


@login_required
def alterar_chamado(request,codigo_chamado):
    chamado = get_object_or_404(Chamado, codigo_chamado=codigo_chamado)
    if request.method == 'POST':
        form = ChamadoForm(request.POST, instance=chamado)
        if form.is_valid():
            form.save()
            messages.success(request, f"Chamado {chamado.protocolo} atualizado.")
            return redirect('index')
    else:
        form = ChamadoForm(instance=chamado)
    return render(request, 'alterar_dados.html',{
        'form':form,
        'chamado':chamado,
    })


@login_required
@require_POST
def excluir_chamado(request, codigo_chamado):
    chamado = get_object_or_404(Chamado, codigo_chamado=codigo_chamado)
    protocolo = chamado.protocolo
    chamado.delete()
    messages.success(request, f"Chamado {protocolo} excluído.")
    return redirect('index')


@login_required
def buscar_chamado(request):
    query = request.GET.get('buscar','').strip()
    chamados = Chamado.objects.filter(
        Q(titulo__icontains=query) |
        Q(solicitante__icontains=query) |
        Q(setor__icontains=query) |
        Q(patrimonio__icontains=query)
    )
    if query.lstrip('#').isdigit():
        chamados = chamados | Chamado.objects.filter(codigo_chamado=int(query.lstrip('#')))
    return render(request, 'index.html', {
        'chamados':chamados,
        'resumo':_resumo(),
        'query':query,
        'status_opcoes':Chamado.STATUS,
    })
