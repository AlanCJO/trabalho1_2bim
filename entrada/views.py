from django.shortcuts import render, redirect
from .models import NotasEntradas
from produto.models import Produtos
from .forms import FormNotasEntradas


def entrada_list(request):

    notas_entrada = NotasEntradas.objects.all()

    template_name = 'entrada_list.html'
    context = {
        'notas_entrada': notas_entrada
    }
    return render(request, template_name, context)


def entrada_new(request):
    if request.method == "POST":
        form = FormNotasEntradas(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.cleaned_data['produto'].quantidade = \
                form.cleaned_data['produto'].quantidade + \
                form.cleaned_data['quantidade']
            form.cleaned_data['produto'].preco = form.cleaned_data['preco']

            form.cleaned_data['produto'].save_base()
            form.save()

            return redirect('entrada:entrada_list')
    else:
        form = FormNotasEntradas()
        template_name = 'entrada_new.html'
        context = {
            'form': form,
        }
        return render(request, template_name, context)


def entrada_update(request, pk):
    nota_entrada = NotasEntradas.objects.get(pk=pk)
    quantidade_anterior = nota_entrada.quantidade
    produto_anterior = nota_entrada.produto
    produto_id = nota_entrada.produto_id

    if request.method == 'POST':
        form = FormNotasEntradas(request.POST, instance=nota_entrada)
        if form.is_valid():
            form.save(commit=False)

            if form.cleaned_data['produto'] == produto_anterior:
                form.cleaned_data['produto'].quantidade += \
                    form.cleaned_data['quantidade'] - quantidade_anterior
            else:
                produto = Produtos.objects.get(pk=produto_id)
                if produto.quantidade >= quantidade_anterior:
                    produto.quantidade = produto.quantidade - quantidade_anterior
                    produto.save()
                form.cleaned_data['produto'].quantidade += form.cleaned_data['quantidade']

            form.cleaned_data['produto'].preco = form.cleaned_data['preco']
            form.cleaned_data['produto'].save_base()
            form.save()

            return redirect('entrada:entrada_list')
    else:
        template_name = 'entrada_update.html'
        context = {
            'form': FormNotasEntradas(instance=nota_entrada),
            'pk': pk
        }

        return render(request, template_name, context)


def entrada_delete(request, pk):
    nota_entrada = NotasEntradas.objects.get(pk=pk)
    quantidade = nota_entrada.quantidade
    produto_id = nota_entrada.produto_id
    nota_entrada.delete()

    produto = Produtos.objects.get(pk=produto_id)
    produto.quantidade = produto.quantidade - quantidade
    produto.save()

    return redirect('entrada:entrada_list')
