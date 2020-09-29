from django.db import models

# Tabla del Alumno


class Alumnoescuela(models.Model):
	nombeApellido=models.CharField(max_length=20, verbose_name="Apellido y Nombre")
	dni=models.CharField(max_length=10, verbose_name="DNI")
	direccion=models.CharField(max_length=50, verbose_name="Dirección")
	email=models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
	telefono=models.CharField(max_length=10, verbose_name="Telefono")
	curso=models.CharField(max_length=10, verbose_name="Curso:")

	def __str__(self):
		return 'DNI:%s; Apellido y Nombre: %s' %(self.dni, self.nombeApellido)


class Docenteescuela(models.Model):
	nombeApellido=models.CharField(max_length=20, verbose_name="Apellido y Nombre")
	dni=models.CharField(max_length=10, verbose_name="DNI")
	direccion=models.CharField(max_length=50, verbose_name="Dirección")
	email=models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
	telefono=models.CharField(max_length=10, verbose_name="Telefono")
	asignatura=models.CharField(max_length=10, verbose_name="Asignatura:")

	def __str__(self):
		return 'DNI:%s; Apellido y Nombre: %s' %(self.dni, self.nombeApellido)
