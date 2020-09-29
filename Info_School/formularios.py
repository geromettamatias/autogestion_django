from django import forms

from .models import Alumnoescuela
from .models import Docenteescuela


class AlumnoescuelaForm(forms.ModelForm):


    class Meta:
        model = Alumnoescuela
        fields = ('nombeApellido','dni','direccion','email','telefono','curso')
        widgets = {
            'nombeApellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'curso': forms.TextInput(attrs={'class':'form-control'})
        }


class DocenteescuelaForm(forms.ModelForm):


    class Meta:
        model = Docenteescuela
        fields = ('nombeApellido','dni','direccion','email','telefono','asignatura')
        widgets = {
            'nombeApellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'asignatura': forms.TextInput(attrs={'class':'form-control'})
        }