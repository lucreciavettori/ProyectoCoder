from django.urls import path
from AppCoder.views import buscar, busquedaCamada, curso, curso_formulario, inicio, estudiantes

urlpatterns = [
    path('curso/', curso, name="AppCoderCurso"),  
    path('inicio/', inicio, name= "AppCoderInicio"),  
    path('estudiantes/', estudiantes, name= "AppCoderEstudiantes"),  
    path('cursoformulario/', curso_formulario, name= "AppCoderCursoFormulario"),  
    path('busquedaCamada/', busquedaCamada, name= "AppCoderBusquedaCamada"), 
    path('buscar/', buscar), 
]
