from django import forms  
from principal.models import FormularioForm  #models.py
     
class FormularioForm(forms.ModelForm):
    class Meta:
        model = FormularioForm
        fields = ['Documento','Numero_Contacto','tipo_sangre','Cargo_Actual','Numero_Emergencia','Fecha_Nacimiento', 'Departamento_Nacimiento','Ciudad_Nacimiento','Ciudad_Residencia','Direccion_Residencia','Sexo','Estado_Civil','Talla_Camisa','Vegetariano','file','Actualmente_Tiene_Restricciones_Laborales_Por_Su_EPS','Actualmente_Se_Encuentra_En_Perdida_De_Capacidad_Laboral','idUser']
        widgets = {
            'idUser': forms.HiddenInput(attrs={'class': 'text-left'}),# Campo oculto
            'Fecha_Nacimiento': forms.DateInput(attrs={'class': 'text-left','type': 'date'}),
             
        }
 
    def __init__(self, *args, **kwargs):
            super(FormularioForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'  



from .models import TuModelo

class TuModeloForm(forms.ModelForm):
    class Meta:
        model = TuModelo
        fields = ['opciones']


# , 'lastname', 'email', 'file', 'fecha_creacion',