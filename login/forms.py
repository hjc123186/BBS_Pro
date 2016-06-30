#-*-coding:utf-8-*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required':"用户名不能为空"},
        widget=forms.TextInput(
            attrs={
                'placeholder':'输入用户名',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='密 码',
        error_messages={'required':"密码不能为空"},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'输入密码',
            }
        ),
    )

    # def clean(self):
    #     if not self.is_valid():
    #         raise forms.ValidationError("错误")
    #     else:
    #         cleaned_data = super(LoginForm,self).clean()


