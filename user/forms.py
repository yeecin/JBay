from django import forms
from django.core.exceptions import ValidationError
from .models import UserInfo

from django.contrib.auth.hashers import make_password


class RegisterForm(forms.ModelForm):
    user_pwd = forms.CharField(widget = forms.PasswordInput ,label = "用户密码")
    confirm_pwd = forms.CharField(widget = forms.PasswordInput ,label = "确认密码")

    class Meta:
        model = UserInfo
        fields = ['user_name' ,'user_pwd' ,'confirm_pwd' ,'user_real_name' ,'user_sex' ,'user_email' ,'user_addr' ,
                  'user_postal_code' ,'user_tel']

    def clean( self ):
        cleaned_data = super().clean()
        pwd = cleaned_data.get('user_pwd')
        confirm_pwd = cleaned_data.get('confirm_pwd')

        if pwd and confirm_pwd and pwd != confirm_pwd:
            raise ValidationError("密码和确认密码不匹配")

        # 将密码转换为哈希值
        hashed_password = make_password(pwd)
        cleaned_data['user_pwd'] = hashed_password

        return cleaned_data
