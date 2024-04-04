from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import GrocesoryForm
from .models import Grocesory


@login_required(login_url="login_url")
def create_order(request):
    template_name = 'grocesoryapp/create.html'
    form = GrocesoryForm()
    if request.method == "POST":
        form = GrocesoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = 'grocesoryapp/show.html'
    orders = Grocesory.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = Grocesory.objects.get(id=pk)
    form = GrocesoryForm(instance=obj)
    if request.method == "POST":
        form = GrocesoryForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, 'grocesoryapp/create.html', context)


def cancel_order(request, pk):
    obj = Grocesory.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'grocesoryapp/confirmation.html')