from django.db import models

# Create your models here.
class Champion(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.CharField(max_length=90)
    tier = models.IntegerField()
    
class Origin(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.CharField(max_length=90)
    description = models.CharField(max_length=150)
    members = models.ManyToManyField(Champion, through='ChampionOrigin')

class ChampionOrigin(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    corigin = models.ForeignKey(Origin, on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.CharField(max_length=90)
    description = models.CharField(max_length=150)
    members = models.ManyToManyField(Champion, through='ChampionClass')

class ChampionClass(models.Model):
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    cclass = models.ForeignKey(Class, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=20)
    img_url = models.CharField(max_length=90)
    description = models.CharField(max_length=150)
