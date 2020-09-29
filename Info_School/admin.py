from django.contrib import admin

from Info_School.models import Alumnoescuela

from Info_School.models import Docenteescuela


class AlumnoAdmin(admin.ModelAdmin):
	# vista tabla
	list_display=("nombeApellido","dni")
	#activar buscador
	search_fields = ["nombeApellido","dni"]

	list_filter= ["curso",]


# separar por curso



admin.site.register(Alumnoescuela, AlumnoAdmin)




class DocenteAdmin(admin.ModelAdmin):
	# vista tabla
	list_display=("nombeApellido","dni")
	#activar buscador
	search_fields = ["nombeApellido","dni"]

	list_filter= ["asignatura",]


# separar por asignatura


admin.site.register(Docenteescuela, DocenteAdmin)


