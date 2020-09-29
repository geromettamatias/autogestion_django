from django.urls import path
from . import views


urlpatterns = [
    path('docente/', views.AutoGestionTablaDocente, name="docente"),
    path('alumno/', views.AutoGestionTablaAlumno, name="alumno"),
   
    path('crearAlumno/', views.CrearAlumno, name="crearAlumno"),
  	path('editarAlumno/<int:persona_id>/', views.EditarAlumno, name="editarAlumno"),
  	path('eliminarAlumno/<int:persona_id>', views.EliminarAlumno,name="eliminarAlumno"),

  	 path('crearDocente/', views.CrearDocente, name="crearDocente"),
  	path('editarDocente/<int:persona_id>/', views.EditarDocente, name="editarDocente"),
  	path('eliminarDocente/<int:persona_id>', views.EliminarDocente,name="eliminarDocente"),
]

