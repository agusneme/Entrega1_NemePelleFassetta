
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from familia.forms import ActualizarProfesorForm, PersonaForm, BuscarPersonasForm, ActualizarPersonaForm, ProfesorForm, ActualizarProfesorForm, CursoForm, ActualizarCursoForm

from familia.models import Persona, Profesor, Curso

# INDEX DE PERSONAS
def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/lista_alumnos.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))
# INDEX DE CURSOS
def index2(request):
    curso = Curso.objects.all()
    template = loader.get_template('familia/lista_cursos.html')
    context = {
        'curso': curso,
    }
    return HttpResponse(template.render(context, request))
# INDEX DE PROFES
def index3(request):
    profesor = Profesor.objects.all()
    template = loader.get_template('familia/lista_profesores.html')
    context = {
        'profesor': profesor,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            edad = form.cleaned_data['edad']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura, edad = edad).save()

            return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar(request, identificador):

    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador=''):

    if request.method == "GET":
        persona = get_object_or_404(Persona, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido, 
            "edad": persona.edad,
            "email": persona.email,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%d/%m/%Y"),
            "altura": persona.altura,
        }
    
        form_actualizar = ActualizarPersonaForm(initial=initial)
        return render(request, 'familia/form_carga.html', {'form': form_actualizar, 'actualizar': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarPersonaForm(request.POST)
        if form_actualizar.is_valid():
            persona = get_object_or_404(Persona, pk=form_actualizar.cleaned_data['id'])
            persona.nombre = form_actualizar.cleaned_data['nombre']
            persona.apellido = form_actualizar.cleaned_data['apellido']
            persona.edad = form_actualizar.cleaned_data['edad']
            persona.email = form_actualizar.cleaned_data['email']
            persona.fecha_nacimiento = form_actualizar.cleaned_data['fecha_nacimiento']
            persona.altura = form_actualizar.cleaned_data['altura']
            persona.save() 

            return HttpResponseRedirect(reverse("index"))


def buscar(request):
    
    if request.GET.get("palabra_a_buscar") and request.method == "GET":
        form_busqueda = BuscarPersonasForm(request.GET)
        if form_busqueda.is_valid():
            personas = Persona.objects.filter(nombre__icontains=request.GET.get("palabra_a_buscar"))
            return  render(request, 'familia/lista_alumnos.html', {"personas": personas, "resultados_busqueda":True})

    elif request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})
        
def front(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/front.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/index.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))    

######### PROFESOR #########

def borrarProfe(request, identificador):

    if request.method == "GET":
        profesor = Profesor.objects.filter(id=int(identificador)).first()
        if profesor:
            profesor.delete()
        return HttpResponseRedirect(reverse("index3"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")




def agregarProfe(request):

    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            profesion = form.cleaned_data['profesion']
            Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion).save()

            return HttpResponseRedirect(reverse("index3"))
    elif request.method == "GET":
        form = ProfesorForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_cargaProfe.html', {'form': form})

def actualizarProfe(request, identificador=''):

    if request.method == "GET":
        profesor = get_object_or_404(Profesor, pk=int(identificador))
        initial = {
            "id": profesor.id,
            "nombre": profesor.nombre, 
            "apellido": profesor.apellido, 
            "profesion": profesor.profesion, 
            "email": profesor.email,
        }
    
        form_actualizar = ActualizarProfesorForm(initial=initial)
        return render(request, 'familia/form_cargaProfe.html', {'form': form_actualizar, 'actualizarProfe': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarProfesorForm(request.POST)
        if form_actualizar.is_valid():
            profesor = get_object_or_404(Profesor, pk=form_actualizar.cleaned_data['id'])
            profesor.nombre = form_actualizar.cleaned_data['nombre']
            profesor.apellido = form_actualizar.cleaned_data['apellido']
            profesor.profesion = form_actualizar.cleaned_data['profesion']
            profesor.email = form_actualizar.cleaned_data['email']
            
            profesor.save() 

            return HttpResponseRedirect(reverse("index3"))


######### CURSO #########

def borrarCurso(request, identificador):

    if request.method == "GET":
        curso = Curso.objects.filter(id=int(identificador)).first()
        if curso:
            curso.delete()
        return HttpResponseRedirect(reverse("index2"))
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")



def agregarCurso(request):

    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            camada = form.cleaned_data['camada']
            Curso(nombre=nombre, camada=camada).save()

            return HttpResponseRedirect(reverse("index2"))
    elif request.method == "GET":
        form = CursoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_cargaCurso.html', {'form': form})

def actualizarCurso(request, identificador=''):

    if request.method == "GET":
        curso = get_object_or_404(Curso, pk=int(identificador))
        initial = {
            "id": curso.id,
            "nombre": curso.nombre, 
            "camada": curso.camada, 
        }
    
        form_actualizar = ActualizarCursoForm(initial=initial)
        return render(request, 'familia/form_cargaCurso.html', {'form': form_actualizar, 'actualizarCurso': True})
    
    elif request.method == "POST":
        form_actualizar = ActualizarCursoForm(request.POST)
        if form_actualizar.is_valid():
            curso = get_object_or_404(Curso, pk=form_actualizar.cleaned_data['id'])
            curso.nombre = form_actualizar.cleaned_data['nombre']
            curso.camada = form_actualizar.cleaned_data['camada']
            curso.save() 
            return HttpResponseRedirect(reverse("index2"))