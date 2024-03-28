from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200)
    prefred_ip = models.CharField(max_length=15)
    alternate_ip = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name