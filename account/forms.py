from django import forms
from django.contrib.auth import forms as auth_forms
from .models import User


class UserCreationForm(forms.ModelForm):

    error_messages = {
        'password_mismatch': "비밀번호가 일치하지 않습니다.",
        'user_id': "해당 프로젝트에 등록된 아이디가 있습니다.",
    }
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")
    class Meta:
        model = User
        fields = ('user_id','user_key','project',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_user_id(self):
        user_id = self.cleaned_data.get("user_id")
        user_key = self.cleaned_data["project"].project_key + "_" + user_id
        try:
            user_instance = User.objects.get(user_key=user_key)
            raise forms.ValidationError(
                self.error_messages['user_id'],
                code='user_id',
            )
        except User.DoesNotExist:
            return user_id

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user_key = self.cleaned_data["project"].project_key + "_" + user.user_id
        user.set_password(self.cleaned_data["password1"])
        user.user_key = user_key

        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]