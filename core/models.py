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

class FileUser(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del archivo")
    filetype = models.CharField(max_length=4, verbose_name="Tipo de archivo")
    path = models.URLField(max_length=500, verbose_name="Link del archivo")

    class Meta:
        verbose_name="Archivo"
    
    def __str__(self) -> str:
        return self.path

class UserPqrsf(models.Model):
    document_type = models.CharField(max_length=1, verbose_name="Tipo de documento", null=True, blank=True)
    document_number = models.CharField(max_length=15, verbose_name="Número de documento", null=True, blank=True)
    fullname = models.CharField(max_length=200, verbose_name="Nombre completo", null=True, blank=True)
    telephone = models.CharField(max_length=10, verbose_name="Número telefónico", null=True, blank=True)
    phone = models.CharField(max_length=10, verbose_name="Número telefónico", null=True, blank=True)
    email = models.EmailField(max_length=500, verbose_name="Email", null=True, blank=True)
    city = models.ForeignKey(City, verbose_name="Ciudad", null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=25, verbose_name="Dirección de residencia", null=True, blank=True)
    associate = models.BooleanField(verbose_name="Asociado", null=True, blank=True)
    agency = models.ForeignKey(Agency, verbose_name="Agencia", null=True, blank=True, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=1, verbose_name="Tipo de petición")
    matter = models.ForeignKey(Matter, verbose_name="Asunto", on_delete=models.CASCADE)
    medium = models.CharField(max_length=1, verbose_name="Medio de respuesta", null=True, blank=True)
    description = models.TextField(max_length=1000, verbose_name="Descripción")
    filing_date = models.DateField(auto_now=False, null=True, blank=True)
    user_type = models.CharField(max_length=1, verbose_name="Tipo de usuario", default="A")
    consumption = models.IntegerField(verbose_name="Consumo", null=True, blank=True)
    token = models.CharField(max_length=1280, verbose_name="Token", null=True, blank=True)
    ticket = models.CharField(max_length=16, verbose_name="Ticket")

    files = models.ManyToManyField(FileUser, verbose_name="Archivos del usuario")

    class Meta:
        verbose_name="Usuario"
    
    def __str__(self) -> str:
        return "{} - {}".format(self.document_number, self.fullname)