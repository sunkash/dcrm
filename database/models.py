from django.db import models

# Create your models here.
class Rides(models.Model):
    name =models.CharField(max_length=255)
    

    class Meta:
        ordering=('name',)
        verbose_name_plural= 'Rides'


    def __str__(self):
        return self.name
