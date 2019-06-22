from account.models import *
from project.models import *
import os

def get_upload_path(instance, filename):
    return os.path.join('project', str(instance.project.project_key), str(instance.user.user_id),filename)

# Create your models here.
class File(models.Model):
    file_key=models.AutoField(primary_key=True, auto_created=True)
    file_name = models.CharField(max_length=100)
    file_path=models.FileField(blank=False,upload_to=get_upload_path)
    user=models.ForeignKey(User,related_name="file",on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="file", on_delete=models.CASCADE)
    expire_min=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일')

    class Meta:
        db_table = 'file'

    def delete(self, *args, **kwargs):
        self.file_path.delete()
        super(File, self).delete(*args, **kwargs)