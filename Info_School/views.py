from django.http import HttpResponse, request
from django.template import Context
from django.template import Template
from django.template import loader
from django.shortcuts import render, redirect

from Info_School.models import Alumnoescuela

from Info_School.models import Docenteescuela


from Info_School.formularios import AlumnoescuelaForm
from Info_School.formularios import DocenteescuelaForm



def AutoGestionTablaAlumno(request):

	nombre="Gerometta Kiewczun"
	alumnos=Alumnoescuela.objects.all()

	return render(request,"tablaAlumno.html", {"usuario":nombre,"alumnos":alumnos})





def CrearAlumno(request):

	

    if request.method == 'POST':
      
        form = AlumnoescuelaForm(request.POST)
      
        if form.is_valid():
        	form.save()
        	return redirect('alumno')
       
    else:
        form = AlumnoescuelaForm()


  
    return render(request, 'crearAlumno.html', {'form': form})



def EditarAlumno(request, persona_id):
    # Recuperamos la instancia de la persona
    instancia = Alumnoescuela.objects.get(id=persona_id)

    # Creamos el formulario con los datos de la instancia
    form = AlumnoescuelaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = AlumnoescuelaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('alumno')

    # Si llegamos al final renderizamos el formulario
    return render(request, "editarAlumno.html", {'form': form})






def EliminarAlumno(request, persona_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Alumnoescuela.objects.get(id=persona_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('alumno')








def AutoGestionTablaDocente(request):

	docentes=Docenteescuela.objects.all()
	nombre="Gerometta Kiewczun"
	

	return render(request,"tablaDocente.html", {"usuario":nombre,"docentes":docentes})






def CrearDocente(request):

	

    if request.method == 'POST':
      
        form = DocenteescuelaForm(request.POST)
      
        if form.is_valid():
        	form.save()
        	return redirect('docente')
       
    else:
        form = DocenteescuelaForm()


  
    return render(request, 'crearDocente.html', {'form': form})



def EditarDocente(request, persona_id):
    # Recuperamos la instancia de la persona
    instancia = Docenteescuela.objects.get(id=persona_id)

    # Creamos el formulario con los datos de la instancia
    form = DocenteescuelaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = DocenteescuelaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('docente')

    # Si llegamos al final renderizamos el formulario
    return render(request, "editarDocente.html", {'form': form})






def EliminarDocente(request, persona_id):
    # Recuperamos la instancia de la persona y la borramos
    instancia = Docenteescuela.objects.get(id=persona_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('docente')









	


