from django import forms  
from principal.models import FormularioForm
from principal.models import aseguramientoForm
from principal.models import familiarForm
# from principal.models import cuidadorHijoForm
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
        fields = ['medicina_prepagada', 'plan_complementario_salud', 'seguro_de_vida', 'seguro_exequial', 'emergencia_medica', 'previser', 'ninguna']
        widgets = {
            'medicina_prepagada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'plan_complementario_salud': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'seguro_de_vida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'seguro_exequial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'emergencia_medica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'previser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ninguna': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FamiliarForm(forms.ModelForm):
    class Meta:
        model = familiarForm
        fields = ['Parentesco_Familiar','Nombres_Familiar','Apellidos_Familiar','Fecha_Nacimiento_Familiar','Convivencia_Hijo','Requiere_Lugar_Para_Llevar_hijo','Discapacidad_Familiar']
        widgets = {
            'Parentesco_Familiar': forms.Select(attrs={'class': 'form-control'}),
            'Nombres_Familiar': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos_Familiar': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_Nacimiento_Familiar': forms.DateInput(attrs={'class': 'text-left','type': 'date'}),
            'Discapacidad_Familiar': forms.Select(attrs={'class': 'form-control'}),
            'Convivencia_Hijo': forms.Select(attrs={'class': 'form-control'}),
            'Requiere_Lugar_Para_Llevar_hijo': forms.Select(attrs={'class': 'form-control'}),
        }

# class CuidadorHijo(forms.ModelForm):
#     class Meta:
#         model = cuidadorHijoForm
#         fields = ['TipoCuidador_Hijo']
#         widgets = {
#             'TipoCuidador_Hijo': forms.Select(attrs={'class': 'form-select'}),
#             'idUser': forms.HiddenInput(),  # Campo oculto para el ID de usuario
#         }




# , 'lastname', 'email', 'file', 'fecha_creacion',