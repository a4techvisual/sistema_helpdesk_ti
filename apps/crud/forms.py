from django import forms
from .models import Chamado


class ChamadoForm(forms.ModelForm):
    class Meta:
        model = Chamado
        fields = ['titulo','solicitante','email','telefone','setor','patrimonio',
                  'categoria','prioridade','status','descricao']
        widgets = {
            'titulo':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"titulo",
                    'placeholder':"Ex.: Notebook não liga",
                    'required':True,
                },
            ),
            'solicitante':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"solicitante",
                    'placeholder':"Nome de quem abriu o chamado",
                    'required':True,
                },
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':"form-control",
                    'id':"email",
                    'placeholder':"nome@empresa.com.br",
                    'required':True,
                },
            ),
            'telefone':forms.TelInput(
                attrs={
                    'class':"form-control",
                    'id':"telefone",
                    'placeholder':"(00) 00000-0000",
                    'required':True,
                },
            ),
            'setor':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"setor",
                    'placeholder':"Ex.: Financeiro",
                    'required':True,
                },
            ),
            'patrimonio':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"patrimonio",
                    'placeholder':"PAT-000000",
                },
            ),
            'categoria':forms.Select(
                attrs={
                    'class':"form-select",
                    'id':"categoria",
                },
            ),
            'prioridade':forms.RadioSelect(
                attrs={
                    'class':"prioridade-radio",
                },
            ),
            'status':forms.Select(
                attrs={
                    'class':"form-select",
                    'id':"status",
                },
            ),
            'descricao':forms.Textarea(
                attrs={
                    'class':"form-control",
                    'id':"descricao",
                    'rows':4,
                    'placeholder':"Descreva o problema, quando começou e o que já foi tentado...",
                    'required':True,
                },
            ),
        }
        error_messages = {
            'patrimonio':{
                'unique': "Já existe um chamado para este patrimônio.",
            },
        }

    def clean_patrimonio(self):
        valor = self.cleaned_data.get('patrimonio')
        return valor or None
