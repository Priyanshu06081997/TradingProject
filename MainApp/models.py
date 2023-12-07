from django.db import models

# Model to upload CSV
class CsvUpload(models.Model):
    file       = models.FileField()
    data       = models.JSONField(blank=True,null=True)