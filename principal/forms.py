from django import forms  
from principal.models import FormularioForm  #models.py
     
class FormularioForm(forms.ModelForm):
    class Meta:
        model = FormularioForm
        fields = ['Documento','Numero_Contacto','tipo_sangre','Cargo_Actual','Numero_Emergencia','Fecha_Nacimiento', 'Departamento_Nacimiento','Sexo','Estado_Civil','Vegetariano','idUser']
        widgets = {
            'idUser': forms.HiddenInput(),# Campo oculto
            'Fecha_Nacimiento': forms.DateInput(attrs={'type': 'date'}),
             
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