from django import forms
from .models import *

class AlergiaForm(forms.ModelForm):
    class Meta:
        model = Alergia
        exclude = ()

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        exclude = ()
