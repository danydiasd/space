from django import forms
class LoginForms(forms.Form):
    
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs= {'class':'form-control', 'placeholder': 'Digite seu email'}),required=True)
    senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput(attrs= {'class':'form-control', 'placeholder': 'Digite sua senha'}), required=True)




class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de Cadastro', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo'}),required=True)
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email'}), required=True)
    senha = forms.CharField(label='Senha', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}), required=True)
    confirmar_senha = forms.CharField(label='Confirmar Senha', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}), required=True)

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
    





