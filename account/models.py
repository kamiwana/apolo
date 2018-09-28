from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import models as auth_models
from project.models import *

class UserManager(auth_models.BaseUserManager):

    def create_user(self,user_key, user_id, project_id, password=None):
        if not user_id:
            raise ValueError('User must have a user id')
        if not user_key:
            raise ValueError('User must have a user key')
        if not project_id:
            raise ValueError('User must have a project id')

        user = self.model(user_id=user_id)
        user.user_key = user_key
        user.project_id = project_id
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_key, user_id, password, project):
        if not user_id:
            raise ValueError("User must have a user id")
        if not user_key:
            raise ValueError('User must have a user key')
        if not project:
            raise ValueError('User must have a project id')

        user = self.create_user(user_key=user_key,user_id=user_id, password=password,project_id=project)

        user.is_superuser = user.is_staff = True
        user.save(using=self._db)
        return user

class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    user_key = models.CharField(max_length=170, unique=True, default='')
    user_id = models.CharField(max_length=64,blank=False)
    user_name = models.CharField(max_length=100, blank=True, verbose_name="사용자 이름")
    project = models.ForeignKey(Project, related_name="project", verbose_name="project_key", on_delete=models.CASCADE)
    variables=models.TextField(max_length=8000)
    is_staff = models.BooleanField(default=False,verbose_name='스태프 권한')
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name='가입일')

    objects = UserManager()

    USERNAME_FIELD = 'user_key'
    REQUIRED_FIELDS = ['user_id','project']

    class Meta:
        verbose_name = '사용자 정보'
        verbose_name_plural ='사용자 정보'
        ordering = ('id', )

    def get_user_name(self):
        return self.user_name