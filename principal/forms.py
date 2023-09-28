from django import forms  
from principal.models import StudentForm  #models.py
     
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentForm
        fields = ['firstname', 'lastname', 'email', 'file', 'fecha_creacion', 'idUser']
        widgets = {
            'idUser': forms.HiddenInput(),  # Campo oculto
        }

 
    def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'  



from .models import TuModelo

class TuModeloForm(forms.ModelForm):
    class Meta:
        model = TuModelo
        fields = ['opciones']


