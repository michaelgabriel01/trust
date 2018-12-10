import hashlib
from django.db import models
from django.contrib.auth.models import AbstractUser

# Client registration model
class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True)
    password1 = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    cpf = models.CharField(max_length=14, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    neighborhood = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    creation_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.email

    @property
    def cpf_public_key(self):
        if self.cpf:
            cpf = hashlib.sha256()
            cpf.update(str(self.cpf).encode('utf-8'))
            cpf.digest()

            return (cpf.hexdigest())
