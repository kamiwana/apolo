from django.db import models
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_key = models.CharField(max_length=64, primary_key=True)
    global_variables=models.TextField(max_length=8000)
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name='수정일')

    class Meta:
        db_table = 'project'

    def __unicode__(self):
        return self.project_key