from django.db import models

# Create your models here.
class Packages(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    dest = models.CharField(max_length=20, blank=True, null=True)
    root = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PACKAGES'