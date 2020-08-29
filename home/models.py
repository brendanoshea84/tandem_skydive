from django.db import models
# Create your models here.


class Enquirer(models.Model):
    default_full_name = models.CharField(max_length=100, null=False, blank=False)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.EmailField(
        max_length=40, null=False, blank=False, default="")
    subject = models.CharField(max_length=200, null=False, blank=False)
    question = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.user.username
