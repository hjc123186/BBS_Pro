#-*-coding:utf-8-*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="�û���",
        error_messages={'required':"�������û���"},
        widget=forms.TextInput(
            attrs={
                'placeholder':'�û���',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='����',
        error_messages={'required':"����������"},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'����',
            }
        ),
    )

    # def clean(self):
    #     if not self.is_valid():
    #         raise forms.ValidationError("�û������벻��Ϊ��")
    #     else:
    #         cleaned_data = super(LoginForm,self).clean()


