from django.db import models
class Trainer(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    def __str__(self):
        return self.name
# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=40, null=False)
    type1 = models.CharField(max_length=30, null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    picture = models.ImageField(upload_to='pokemon_images', null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return  self.name
    