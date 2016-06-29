#-*-coding:utf-8-*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required':"请输入用户名"},
        widget=forms.TextInput(
            attrs={
                'placeholder':'用户名',
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label='密码',
        error_messages={'required':"请输入密码"},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'密码',
            }
        ),
    )

    # def clean(self):
    #     if not self.is_valid():
    #         raise forms.ValidationError("用户和密码不能为空")
    #     else:
    #         cleaned_data = super(LoginForm,self).clean()


