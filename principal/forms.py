from django import forms  
from principal.models import FormularioForm, aseguramientoForm, familiarForm, familiardiscapacidadForm, situacionesafectableForm, mascotasForm, transorteForm, recursosdigitales, appaprendizajeForm, ofrecimientoForm , desarrollopersonalForm, reconocimientoempresarialForm, actividadesculturalesForm
from django.forms import modelformset_factory
     
class FormularioForm(forms.ModelForm):
    class Meta:
        model = FormularioForm
        fields = ['Tipo_Documento','Documento','Numero_Contacto','tipo_sangre','Cargo_Actual','Numero_Emergencia','Fecha_Nacimiento', 'Departamento_Nacimiento','Ciudad_Nacimiento','Ciudad_Residencia','Direccion_Residencia','Sexo','Estado_Civil','Etnia','Talla_Camisa','Vegetariano','file','Actualmente_Tiene_Restricciones_Laborales_Por_Su_EPS','Actualmente_Se_Encuentra_En_Perdida_De_Capacidad_Laboral','Pensionado','Discapacidad_Familiar','Tipo_Vivienda','Estrato_Vivienda','Tiempo_Desplazamiento','Tiempo_Vinculacion_Laboral','Tiempo_Cargo_Laboral','Nivel_Educativo_Mas_Alto','Ultimo_Nivel_Educativo','Tipo_Contrato_Form','Horario_laboral','Horas_Laborales','Promedio_Ingresos','idUser']
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
        fields = ['Parentesco_Familiar','Nombres_Familiar','Apellidos_Familiar','Fecha_Nacimiento_Familiar','Convivencia_Hijo','Requiere_Lugar_Para_Llevar_hijo','Sexo_Familiar','Dependiente_Economico']
        widgets = {
            'Parentesco_Familiar': forms.Select(attrs={'class': 'form-control'}),
            'Dependiente_Economico': forms.Select(attrs={'class': 'form-control'}),
            'Sexo_Familiar': forms.Select(attrs={'class': 'form-control'}),
            'Nombres_Familiar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres del familiar'}),
            'Apellidos_Familiar': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Apellidos del familiar'}),
            'Fecha_Nacimiento_Familiar': forms.DateInput(attrs={'class': 'form-control','type': 'date'}),
            'Convivencia_Hijo': forms.Select(attrs={'class': 'form-control'}),
            'Requiere_Lugar_Para_Llevar_hijo': forms.Select(attrs={'class': 'form-control'}),
        }

class FamiliarDiscapacidadForm(forms.ModelForm):
    class Meta:
        model = familiardiscapacidadForm
        fields = ['padre','madre','hijo','hija','abuelo','abuela','nieto','nieta','hermano','hermana','tio','tia','primo','prima','sobrino','sobrina','cuñado','cuñada','suegro','suegra','yerno','nuera','esposo','esposa','Ninguno']
        widgets = {
        'padre' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'madre' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'hijo' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'hija' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'abuelo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'abuela': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'nieto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'nieta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'hermano': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'hermana': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'tio' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'tia'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'primo'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'prima'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'sobrino'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'sobrina'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'cuñado'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'cuñada'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'suegro'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'suegra'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'yerno'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'nuera'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'esposo'    : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'esposa'   : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Ninguno'  : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class SituacionesAfectableForm(forms.ModelForm):
    class Meta:
        model = situacionesafectableForm
        fields = ['Problemas_de_conducta','Muerte_reciente_de_mascotas', 'Consumo_de_sustancias_psicoactivas', 'Muerte_reciente_de_personas_cercanas', 'Desempleo', 'Enfermedad_de_algún_familiar', 'Deudas_que_superan_los_ingresos', 'Dificultad_para_acceder_a_educación', 'Problemas_intrafamiliares', 'Problemas_de_pareja','Ninguna_situacion_afectable']
        widgets = {
       'Muerte reciente de mascotas' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Consumo de sustancias psicoactivas' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Muerte reciente de personas cercanas' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Desempleo' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Enfermedad de algún familiar' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Deudas que superan los ingresos' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Dificultad para acceder a educación' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Problemas intrafamiliares' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Problemas de pareja' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Ninguna_situacion_afectable' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Problemas_de_conducta' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MascotasForm(forms.ModelForm):
    class Meta:
        model = mascotasForm
        fields = ['Tipo_Mascota', 'Nombre_Mascota']
        widgets = {
            'Tipo_Mascota': forms.Select(attrs={'class': 'form-control'}),
            'Nombre_Mascota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la mascota'}),
        }

    def clean_Nombre_Mascota(self):
        nombre_mascota = self.cleaned_data.get('Nombre_Mascota')
        if not nombre_mascota:
            raise forms.ValidationError("Este campo es obligatorio.")
        return nombre_mascota

class TransportesForm(forms.ModelForm):
    class Meta:
        model = transorteForm
        fields = ['Caminando','Bicicleta','Moto','Carro','Comparto_Vehiculo','Transporte_Publico','Taxi','Plataforma_movilidad_Uber_Didi','Patineta','Modalidad_Virtual']
        widgets = {
       'Caminando' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Bicicleta' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Moto' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Carro' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Comparto_Vehiculo' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Transporte_Publico' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Taxi' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Plataforma_movilidad_Uber_Didi' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Patineta' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Modalidad_Virtual' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
       'Problemas_de_conducta' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class RecursosDigitalesForm(forms.ModelForm):
     class Meta:
        model = recursosdigitales
        fields = ['Microsoft_OneDrive_Google_Drive', 'Microsoft_o_Google_Calendar','Microsoft_PowerBI', 'Sharepoint', 'Microsoft_Sway', 'Microsoft_Forms', 'Microsoft_Excel', 'Microsoft_Planner', 'Microsoft_Power_Automate', 'Microsoft_Project', 'Microsoft_Teams', 'Microsoft_Yammer', 'Kahoot', 'Google_Formularios', 'Google_Jamboard', 'Slack', 'Google_Padlet', 'Google_Meet', 'Google_Classroom', 'Google_Drawing', 'Google_Sites', 'Google_Blogger', 'Google_Earth', 'Google_Collections', 'Google_Currents', 'Google_Docs', 'Google_Sheets', 'Google_Slides', 'Google_Expeditions', 'Asana', 'Trello', 'VPN', 'Camscanner']
        widgets = {
       'Microsoft_OneDrive_Google_Drive': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_o_Google_Calendar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_PowerBI': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Sharepoint': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Sway': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Forms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Excel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Planner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Power_Automate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Project': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Teams': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Yammer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Kahoot': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Formularios': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Jamboard': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Slack': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Padlet': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Meet': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Classroom': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Drawing': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Sites': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Blogger': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Earth': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Collections': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Currents': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Docs': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Sheets': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Slides': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Expeditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Asana': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Trello': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'VPN': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Camscanner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class AppAprendizajeForm(forms.ModelForm):
     class Meta:
        model = appaprendizajeForm
        fields = ['Microsoft_OneDrive_Google_Drive', 'Microsoft_o_Google_Calendar','Microsoft_PowerBI', 'Sharepoint', 'Microsoft_Sway', 'Microsoft_Forms', 'Microsoft_Excel', 'Microsoft_Planner', 'Microsoft_Power_Automate', 'Microsoft_Project', 'Microsoft_Teams', 'Microsoft_Yammer', 'Kahoot', 'Google_Formularios', 'Google_Jamboard', 'Slack', 'Google_Padlet', 'Google_Meet', 'Google_Classroom', 'Google_Drawing', 'Google_Sites', 'Google_Blogger', 'Google_Earth', 'Google_Collections', 'Google_Currents', 'Google_Docs', 'Google_Sheets', 'Google_Slides', 'Google_Expeditions', 'Asana', 'Trello', 'VPN', 'Camscanner']
        widgets = {
       'Microsoft_OneDrive_Google_Drive': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_o_Google_Calendar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_PowerBI': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Sharepoint': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Sway': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Forms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Excel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Planner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Power_Automate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Project': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Teams': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Microsoft_Yammer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Kahoot': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Formularios': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Jamboard': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Slack': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Padlet': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Meet': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Classroom': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Drawing': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Sites': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Blogger': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Earth': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Collections': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Currents': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Docs': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Sheets': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Slides': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Google_Expeditions': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Asana': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Trello': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'VPN': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Camscanner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OfrecimientosForm(forms.ModelForm):
    class Meta:
        model = ofrecimientoForm
        fields = ['reconocimiento','compensacion_economica','actividades_de_voluntariado','actividades_deportivas_recreacionales','actividades_artisticas_culturales','actividades_integracion_familiar','patrocinios_educativos','programas_situaciones_familiares','convenios_acceder_cursos_programas']
        widgets = {
        
        'reconocimiento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'compensacion_economica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'actividades_de_voluntariado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'actividades_deportivas_recreacionales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'actividades_artisticas_culturales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'actividades_integracion_familiar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'patrocinios_educativos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'programas_situaciones_familiares': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'convenios_acceder_cursos_programas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
        
class DesarrolloPersonalForm(forms.ModelForm):
    class Meta:
        model = desarrollopersonalForm
        fields = ['Salud_financiera', 'Relaciones_familiares', 'Manejo_de_conflictos', 'Manejo_de_adicciones', 'Manejo_del_duelo', 'Estilos_de_vida_saludable', 'Salud_mental', 'Cuidado_parental', 'Enfermedades_crónicas', 'Enfermedades_de_transmisión_sexual', 'Prevención_y_manejo_del_cáncer', 'Expresión_oral_y_corporal']
        widgets = {
        
        'Salud_financiera': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Relaciones_familiares': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Manejo_de_conflictos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Manejo_de_adicciones': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Manejo_del_duelo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Estilos_de_vida_saludable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Salud_mental': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Cuidado_parental': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Enfermedades_crónicas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Enfermedades_de_transmisión_sexual': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Prevención_y_manejo_del_cáncer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Expresión_oral_y_corporal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

    }
        
class ReconocimientoEmpresarialForm(forms.ModelForm):
    class Meta:
        model = reconocimientoempresarialForm
        fields = ['Participar_en_iniciativas_o_proyectos', 'Viajes', 'Bonos_en_dinero', 'Flexibilidad_horaria', 'Tiempo_libre', 'Patrocinios_para_formación_profesional', 'Patrocinios_para_desarrollo_personal', 'Bonos_actividades_recreación']
        widgets = {
        
        'Participar_en_iniciativas_o_proyectos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Viajes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Bonos_en_dinero': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Flexibilidad_horaria': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Tiempo_libre': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Patrocinios_para_formación_profesional': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Patrocinios_para_desarrollo_personal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Bonos_actividades_recreación': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
        
class ActividadesCulturalesForm(forms.ModelForm):
    class Meta:
        model = actividadesculturalesForm
        fields = ['Conciertos', 'Exposiciones', 'Teatro', 'Cine', 'Leer_club_de_lectura', 'Bailar', 'Ver_televisión', 'Viajar', 'Pintar', 'Mandalas', 'Escritura', 'Bordado', 'Gastronomía', 'Canto', 'Escultura', 'Fotografía', 'Cerámica', 'Interpretación_musical', 'Ninguna']
        widgets = {
        
        'Conciertos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Exposiciones': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Teatro': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Cine': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Leer_club_de_lectura': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Bailar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Ver_televisión': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Viajar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Pintar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Mandalas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Escritura': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Bordado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Gastronomía': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Canto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Escultura': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Fotografía': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Cerámica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Interpretación_musical': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'Ninguna': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
# , 'lastname', 'email', 'file', 'fecha_creacion',m