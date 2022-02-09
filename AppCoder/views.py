from django.shortcuts import render
from AppCoder.forms import CursoFormulario
from AppCoder.models import Curso


# Create your views here.
def curso (request):
    return render(request,'AppCoder/curso.html')

def inicio (request):
    return render(request,'AppCoder/index.html')

def estudiantes (request):
    return render(request,'AppCoder/estudiantes.html')

#def curso_formulario(request):
    
    #if request.method == 'POST':
            #r_curso = request.POST['curso']
            #r_camada = request.POST['camada']
            #curso = Curso(nombre=r_curso, camada=r_camada)
            #curso.save()
    
    #return render(request, 'AppCoder/curso_formulario.html')

def curso_formulario(request):
    
    if request.method == 'POST':
        
        miFormulario = CursoFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.data
            
            r_curso = informacion['nombre']
            r_camada = informacion['camada']
        
            curso = Curso(nombre=r_curso, camada=r_camada)
            curso.save()
    
    miFormulario = CursoFormulario()

    return render(request, 'AppCoder/curso_formulario.html', {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html' )

def buscar(request):
    
    if request.GET['camada']:
        camada =request.GET ['camada']
        cursos =Curso.objects.filter(camada__icontains=camada)
    
        return render(request, 'AppCoder/resultadosPorBusqueda.html', { "cursos":  cursos,"camada": camada })
    else:

        respuesta ="No enviar datos"

    return render(request, 'AppCoder/resultadosPorBusqueda.html')