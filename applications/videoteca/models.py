from django.db import models

# Create your models here.
class Bboy(models.Model):
    name = models.CharField('Bboy',max_length=80)
    nacionalidad = models.CharField('Pais',blank=True,max_length=80)

    def __str__(self):
        return self.name


class Powermove(models.Model):
    name = models.CharField('Movimiento', max_length=80)
    resume = models.TextField('Resumen',blank=True)
    bboy = models.ManyToManyField(Bboy)

    def __str__(self):
        return self.name


