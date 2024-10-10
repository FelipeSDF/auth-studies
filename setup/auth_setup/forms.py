from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models

class RegisterFieldsValidators:

    def username_validator(username):
        ...
    def password_validator(password):
        if len(password) < 8:
            raise ValidationError(message='a senha deve ter pelo menos 8 digitos', code='invalid')

class LoginFieldsValidators:
    def user_exists_validator(username):
        users = User.objects.filter(username = username)
        if not users:
            raise ValidationError('Usuário não encontrado!')
        
class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        widget= forms.TextInput(),
    )
    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(),
        validators=[RegisterFieldsValidators.password_validator],
    )
    confirm_password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(),
        validators=[RegisterFieldsValidators.password_validator],
        
    )
    
    class Meta:
        model = User
        fields = ['username','password']
        
    def clean_username(self):
        data = self.cleaned_data.get('username')
        
        if len(data) > 10 or len(data) < 10:
            raise ValidationError('Digite um username de 10 digitos')
        
        return data

    def clean(self):
        cleaned_data =  super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError({
                'password':'as senhas devem ser iguais',
                'confirm_password':'as senhas devem ser iguais'
            })
        
        return super().clean()

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget= forms.TextInput(attrs={
            'id':'username_field',
            'class':'form_field_input'}),
    )
    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={
            'id':'password_field',
            'class':'form_field_input'}),
    )
    def clean(self) -> dict[str, Any]:
        from django.contrib.auth import authenticate, login
        data = self.cleaned_data.get('password')
        
        authenticated = authenticate(
        username=self.cleaned_data.get('username',''),
        password=self.cleaned_data.get('password','')
        )
        if not authenticated:
            raise ValidationError({
                'username':'Usuário ou senha inválidos',
                'password':'Usuário ou senha inválidos'
                })
        return super().clean()
    
class PostForm(forms.ModelForm):
    tittle = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
                'type':'disabled',
                'class':'form_field_input'
            }
        )
    )
    date = forms.CharField(widget=forms.TextInput(attrs={
        'type':'date',
        'id':'form_date_input',
        'class':'form_field_input'
    }))
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'id':'form_textarea_input',
            'class':'form_field_textarea'
        }))
    class Meta:
        model = models.PostModel
        fields = ['user','tittle','date','text']
        
        labels = {
            'user':'Quem está escrevendo?'
        }
        
        widgets = {
        }
        
















# class RegisterForm(forms.ModelForm):
#     brabo = forms.CharField(
#         required=True,
#         widget = forms.PasswordInput(attrs= {
#             'placeholder':'password na mao' 
#         }),
        
#         label= 'bagulhodoido'
#     )
    
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password',
#             ]
        
#         labels = {
#         }
        
#         help_texts = {
#             'username': ''
#         }
    

    
#     def clean_brabo(self):
#         data = self.cleaned_data.get('brabo')
        
#         if 'teste' in data:
#             raise ValidationError(
#                 'não digite %(value)s',
#                 code='invalid',
#                 params={'value':'teste'}
#             )

#         return data
#     def clean(self):
#         cleaned_data = super().clean()
#         brabo = cleaned_data.get('brabo')
#         password = cleaned_data.get('password')
        
#         print(brabo, password)
#         if brabo != password:
#             raise ValidationError({
#                 'brabo':ValidationError('ta errado po', code='invalid'),
#                 'password':'tem que estar igual essa porra'
#             })