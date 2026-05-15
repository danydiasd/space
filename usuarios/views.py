from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    
    
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            # Process the valid form data
            pass
    else:
        form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {'form': form})
           
