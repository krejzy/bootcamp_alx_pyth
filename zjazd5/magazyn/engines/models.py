from django.db import models

# Create your models here.

class Engine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    engine capacity = models.IntegerField()
    number of cylinders = models.IntegerField()
    model = models.TextField()
    combustion cycle = models.IntegerField()
    engine = models.TextField()
    is avalible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " " + self.name

