from django.shortcuts import render, redirect
from .models import NotasEntradas
from .forms import FormNotasEntradas


def entrada_list(request):

    nota_entrada = NotasEntradas.objects.all()

    template_name = 'entrada_list.html'
    context = {
        'nota_entrada': nota_entrada
    }
    return render(request, template_name, context)


def entrada_new(request):
    print("METODO --> ", request.method)
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
