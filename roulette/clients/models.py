from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField("Nome do cliente", max_length=255)
    cpf = models.CharField("CPF", max_length=50, blank=True, null=True)
    email = models.CharField("E-mail", max_length=255, blank=True, null=True)
    fone = models.CharField("Telefone", max_length=50, blank=True, null=True)
    created_at = models.DateTimeField("Registrado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    
    
    def __str__(self):
        return f'{self.name}{"- " + self.fone if self.fone else ""}'
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'