from django.db import models

class Roulette(models.Model):
    name = models.CharField("Nome da rifa", max_length=50)
    max_numbers = models.SmallIntegerField("Quantidade máxima de números", default=50)
    file = models.FileField("Imagem da rifa", max_length=4000, blank=True, null=True)
    spins = models.SmallIntegerField("Quantidade de giros", default=0, blank=True)
    created_at = models.DateTimeField("Registrado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Rifa'
        verbose_name_plural = 'Rifas'
    
    
class RouletteNumber(models.Model):
    roulette = models.ForeignKey(Roulette, verbose_name=("Rifa"), on_delete=models.CASCADE)
    client = models.ForeignKey("clients.Client", verbose_name=("Cliente"), on_delete=models.CASCADE)
    number = models.CharField("Número do bilhete", max_length=50)
    created_at = models.DateTimeField("Registrado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    
    def __str__(self):
        return f'{self.number} - {self.client}'
    
    class Meta:
        verbose_name = 'Número da sorte'
        verbose_name_plural = 'Números da sorte'

# Create your models here.
class RouletteWinner(models.Model):
    roulette = models.ForeignKey(Roulette, verbose_name=("Rifa"), on_delete=models.CASCADE)
    winner = models.ForeignKey("clients.Client", verbose_name=("Vencedor"), on_delete=models.CASCADE)
    number = models.CharField("Número do bilhete premiado", max_length=50, default="")
    created_at = models.DateTimeField("Registrado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    
    def __str__(self):
        return f'{self.winner}'
    
    class Meta:
        verbose_name = 'Ganhador'
        verbose_name_plural = 'Ganhadoress'