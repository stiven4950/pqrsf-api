from django.db import models

# Create your models here.
class City(models.Model):
    municipioId = models.CharField(verbose_name="Id Municipio", max_length=5)
    municipioDepartamento = models.CharField(verbose_name="Ciudad con departamento", max_length=256)

    class Meta:
        verbose_name="Ciudades"
        ordering=['pk']
    
    def __str__(self) -> str:
        return self.municipioDepartamento

class Agency(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=256)

    class Meta:
        verbose_name="Agencia"
        ordering=['pk']
    
    def __str__(self) -> str:
        return self.name

class Matter(models.Model):
    matter_type = models.CharField(verbose_name="Tipo de petición", max_length=1)
    name = models.CharField(verbose_name="Nombre", max_length=256)

    class Meta:
        verbose_name="Asunto"
    
    def __str__(self) -> str:
        return self.name