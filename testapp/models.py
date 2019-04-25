from django.db import models

# Create your models here.


class Testmodel(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)

    def approve(self):
        self.save()
