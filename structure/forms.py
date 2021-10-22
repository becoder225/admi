from django import forms
from django.forms import ModelForm
from structure.models import *
from django.contrib.auth import get_user_model


class StructureForm(ModelForm):
    TYPE_STRUCTURE = (
        ('2', 'STRUCTURE DE SANTE'),
        ('1', 'PHARMACIE'),

    )
    PAYS_VALUE = (
        ('1', 'COTE D\'IVOIRE'),
        ('2', 'FRANCE'),
    )
    typeStructure = forms.ChoiceField(choices=TYPE_STRUCTURE)
    pays = forms.ChoiceField(choices=PAYS_VALUE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['telephone'].label = ""
        self.fields['telephone'].widget.attrs.update({
            'placeholder': '0701 010 101'
        })
    def clean(self):
        cleaned_data = super(StructureForm, self).clean()
        # additional cleaning here
        typeStructure = cleaned_data.get("typeStructure")
        print(typeStructure)
        if typeStructure == "2" :
            print(typeStructure)
            if not cleaned_data.get("typestructureSante"):
                self.add_error('typestructureSante', "Ce champ est Obligatoire")
               # raise forms.ValidationError('Ce champ est Obligatoire.')

    class Meta:
        model = StructureSante
        fields = '__all__'
        exclude = ('logo', 'professionelSante', 'structureParent')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 20, 'rows': 2}),

             #'immatriculation': forms.TextInput(attrs={'placeholder': 'par Ex: 1797 WS CI 01'}),
        }



class PersonelForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'birthday', 'sexe', 'email', 'phone', 'adresse')
        # exclude = ('username','password' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['phone'].label = ""
        self.fields['phone'].widget.attrs.update({
            'placeholder': 'Telephone'
        })


class AgentStructureForm(ModelForm):
    class Meta:
        model = AgentStructure
        fields = '__all__'
        exclude = ('user', 'structureSante')


class ProfessionelSanteForm(ModelForm):
    class Meta:
        model = ProfessionelSante
        fields = '__all__'
        exclude = ('user', 'structureSante')

class SearchPsForm(forms.Form):
    matricule = forms.CharField(max_length=100,required=False)
    num_ordre = forms.CharField(max_length=100,required=False)
    tel = forms.CharField(max_length=100, required=False)
