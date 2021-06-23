from django.shortcuts import render, redirect
from .models import NotaSaida
from produto.models import Produtos
from .forms import FormNotaSaida


def nota_saida_list(request):
    notas_saida = NotaSaida.objects.all()
    template_name = 'notasaida_list.html'
    context = {'notas_saida': notas_saida}

    return render(request, template_name, context)


def nota_saida_new(request):
    if request.method == 'POST':
        form = FormNotaSaida(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = \
                form.cleaned_data['produto'].quantidade - \
                form.cleaned_data['quantidade']
            form.cleaned_data['produto'].preco = form.cleaned_data['valor']

            form.cleaned_data['produto'].save_base()
            form.save()

            return redirect('notaSaida:saida_list')
    else:
        form = FormNotaSaida()
        template_name = 'notasaida_new.html'
        context = {'form': form}

        return render(request, template_name, context)


def nota_saida_update(request, pk):
    nota_saida = NotaSaida.objects.get(pk=pk)
    quantidade_anterior = nota_saida.quantidade
    produto_anterior = nota_saida.produto
    produto_id = nota_saida.produto_id

    if request.method == 'POST':
        form = FormNotaSaida(request.POST, instance=nota_saida)
        if form.is_valid():
            form.save(commit=False)

            if form.cleaned_data['produto'] == produto_anterior:
                form.cleaned_data['produto'].quantidade -= \
                    form.cleaned_data['quantidade'] - quantidade_anterior
            else:
                produto = Produtos.objects.get(pk=produto_id)
                if produto.quantidade >= quantidade_anterior:
                    produto.quantidade = produto.quantidade + quantidade_anterior
                    produto.save()
                form.cleaned_data['produto'].quantidade -= form.cleaned_data['quantidade']

            form.cleaned_data['produto'].valor = form.cleaned_data['valor']
            form.cleaned_data['produto'].save_base()
            form.save()

            return redirect('notaSaida:saida_list')
    else:
        template_name = 'notasaida_update.html'
        context = {
            'form': FormNotaSaida(instance=nota_saida),
            'pk': pk
        }

        return render(request, template_name, context)


def nota_saida_delete(request, pk):
    nota_saida = NotaSaida.objects.get(pk=pk)
    quantidade = nota_saida.quantidade
    produto_id = nota_saida.produto_id
    nota_saida.delete()

    produto = Produtos.objects.get(pk=produto_id)
    produto.quantidade = produto.quantidade + quantidade
    produto.save()

    return redirect('notaSaida:saida_list')
