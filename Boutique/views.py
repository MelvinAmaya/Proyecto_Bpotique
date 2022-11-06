from django.shortcuts import render

# Create your views here.

def ruta(peticion):
    return render(peticion,'index.html')
    
    
def ruta2(peticion):
    return render(peticion,'about.html')