from django.db import models
import uuid


# Create your models here.
class Vegetable(models.Model):
    CATEGORIES = {
        'NONE': "-",
        'Root': "Root",
        'Stem': "Stem",
        'Bulb': "Bulb",
        'Leaf': "Leaf",
        'Fruit': "Fruit",
        'Flower': "Flower",
        'Seed': "Seed",
        'Tuber': "Tuber",
    }

    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25, unique=True)
    calorie = models.PositiveSmallIntegerField(blank=False)
    kilojoule = models.PositiveSmallIntegerField(blank=False)
    category = models.CharField(max_length=20, choices=CATEGORIES, default='None')
    wiki = models.URLField(null=True)

    def __str__(self):
        return self.name