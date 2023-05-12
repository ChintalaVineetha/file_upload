from django.db import models

class File(models.Model):
  file = models.FileField(blank=False, null=False)
  file.uploaded_at = models.DateTimeField(auto_now_add=True)
  class Meta:
    db_table= "data1"
