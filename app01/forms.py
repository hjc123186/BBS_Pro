#-*-coding:utf8-*-
from django import forms
from models import Category
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class BBS_sub_form(forms.Form ):
    category = forms.ModelChoiceField(
        label='版块',
        queryset=Category.objects.all(),
        required=True,
        error_messages={'required':"请选择"},
    )
    title = forms.CharField(
        label='标题',
        max_length=64,
        required=True,
        error_messages={'required':"标题不能为空"},
    )
    summary = forms.CharField(
        label='摘要',
        max_length=256,
        required=True,
    )


    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("错误")
        else:
            cleaned_data = super(BBS_sub_form,self).clean()
