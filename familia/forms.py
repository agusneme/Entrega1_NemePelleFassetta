from django import forms

#### Persona 

class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))
    edad = forms.IntegerField(label="Edad")

class ActualizarPersonaForm(PersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())


class BuscarPersonasForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")


#### Profesor

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)

class ActualizarProfesorForm(ProfesorForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

#### Curso

class CursoForm(forms.Form):

    nombre = forms.CharField(max_length=50)
    camada = forms.CharField(max_length=50)

class ActualizarCursoForm(CursoForm):
    id = forms.IntegerField(widget = forms.HiddenInput())