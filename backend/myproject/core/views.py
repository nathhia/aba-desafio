'''
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
'''
from django.shortcuts import render, redirect
from .models import Funcionario 
from .forms import FuncionarioForm



def list_func(request):
	funcionarios = Funcionario.objects.all()
	return render(request, 'funcionarios.html', {'funcionarios' : funcionarios})

def create_func(request):
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/list_func/')

    return render(request, 'funcionarios-form.html', {'form': form})

def update_func(request, id):
	funcionario = Funcionario.objects.get(id=id)
	form = FuncionarioForm(request.POST or None, instance=funcionario)

	if form.is_valid():
		form.save()
		return redirect('/list_func/')

	return render(request, 'funcionarios-form.html', {'form': form, 'funcionario': funcionario})

def delete_func(request, id):
	funcionario = Funcionario.objects.get(id=id)

	if request.method == 'POST':
		funcionario.delete()
		return redirect('/list_func/')

	return render(request, 'func-delete-confirm.html', {'funcionario': funcionario})

def info_func(request, id):
	funcionario = Funcionario.objects.get(id=id)
	return render(request, 'funcionario.html', {'funcionario': funcionario})
