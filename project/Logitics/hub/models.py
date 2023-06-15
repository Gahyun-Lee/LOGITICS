from django.db import models

# Create your models here.
class Hubs(models.Model):
    name = models.CharField(max_length=20)
    dest = models.CharField(max_length=20)
    weight = models.IntegerField()
    que = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'HUBS'
        
    def get_absolute_url(self):
        return f'{self.pk}/'
    