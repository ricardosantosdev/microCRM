from .models import Clients
from .forms import ClientsForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

@login_required(login_url='/login')
def read_clients(request):
    clients = Clients.objects.all()
    return render(request, 'clients/clients.html', {"clients": clients})

@login_required(login_url='/login')
def new_client(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('clients')
    form = ClientsForm()
    return render(request, 'clients/form-client.html', {"form": form})

@login_required(login_url='/login')
def edit_client(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientsForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients')
    return render(request, 'clients/form-client.html', {"form": form})

@login_required(login_url='/login')
def delete_client(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientsForm(request.POST or None, instance=client)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')
    return render(request, 'clients/confirmation.html', {"client": client})
