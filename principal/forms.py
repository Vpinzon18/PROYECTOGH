from django import forms  
from principal.models import FormularioForm
from principal.models import aseguramientoForm
from principal.models import HijoForm
from django.forms import modelformset_factory
     
class FormularioForm(forms.ModelForm):
    class Meta:
        model = FormularioForm
        fields = ['Tipo_Documento','Documento','Numero_Contacto','tipo_sangre','Cargo_Actual','Numero_Emergencia','Fecha_Nacimiento', 'Departamento_Nacimiento','Ciudad_Nacimiento','Ciudad_Residencia','Direccion_Residencia','Sexo','Estado_Civil','Etnia','Talla_Camisa','Vegetariano','file','Actualmente_Tiene_Restricciones_Laborales_Por_Su_EPS','Actualmente_Se_Encuentra_En_Perdida_De_Capacidad_Laboral','Pensionado','idUser']
        widgets = {
            'idUser': forms.HiddenInput(attrs={'class': 'text-left'}),# Campo oculto
            'Fecha_Nacimiento': forms.DateInput(attrs={'class': 'text-left','type': 'date'}),
             
        }
 
    def __init__(self, *args, **kwargs):
            super(FormularioForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'  


class AseguramientoForm(forms.ModelForm):
    class Meta:
        model = aseguramientoForm
        fields = ['Tipo_Aseguramiento']
        widgets = {
            'Tipo_Aseguramiento': forms.Select(attrs={'class': 'form-select'}),
            'idUser': forms.HiddenInput(),  # Campo oculto para el ID de usuario
        }


class HijosForm(forms.ModelForm):
    class Meta:
        model = HijoForm
        fields = ['Nombres_Hijo','Apellido_Hijo','Fecha_Nacimiento_Hijo','Cuidador_Hijo','Convivencia_Hijo','Requiere_Lugar_Para_Llevar_hijo']
        widgets = {
            
            'Requiere_Lugar_Para_Llevar_hijo': forms.Select(attrs={'class': 'form-select'}),
            'idUser': forms.HiddenInput(),  # Campo oculto para el ID de usuario
            'Fecha_Nacimiento_Hijo': forms.DateInput(attrs={'class': 'text-left','type': 'date'}),
        }






# , 'lastname', 'email', 'file', 'fecha_creacion',