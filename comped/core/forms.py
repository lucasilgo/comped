from django import forms

class CadastrarPacienteForm(forms.Form):
    nome = forms.CharField()
    cpf = forms.CharField()
    data_nascimento = forms.DateField()
    convenio = forms.CharField()
    pratica_esporte = forms.BooleanField()
    profissao = forms.CharField()
    sexo = forms.CharField()
    email = forms.EmailField()
    tel_fixo = forms.CharField()
    tel_cel = forms.CharField()