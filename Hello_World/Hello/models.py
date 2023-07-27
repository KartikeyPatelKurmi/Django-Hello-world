from django.db import models

class HelloWorldModel(models.Model):
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.message