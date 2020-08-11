from django.db import models

# Create your models here.

class JumperDetail(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)     

    def __str__(self):
        return self.user.username