from django.db import models

# Create your models here.


class Enquirer(models.Model):
    Name = models.CharField(max_length=100, null=False, blank=False)
    Phone_Number = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(
        max_length=40, null=False, blank=False, default="")
    Subject = models.CharField(max_length=200, null=False, blank=False)
    Question = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
