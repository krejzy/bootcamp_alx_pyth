from django.db import models
# Create your models here.

TYP NADWOZIA
("kombi", "kombi"),
("sedan", "sedan")
("terenowy", "terenowy"),
("van", "van")



class Cars(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    year of production = models.IntegerField()
    mark = models.TextField()
    model = models.TextField()
    type of body = models.TextField()
    engine = models.TextField()
    is avalible = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " " + self.name

