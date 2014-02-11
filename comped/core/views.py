from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def home_secretaria(request):
    return render(request, 'index_secretaria.html')

def home_medico(request):
    return render(request, 'index_medico.html')

def cadastrar_paciente(request):
    return render(request, 'cadastrar_paciente.html')