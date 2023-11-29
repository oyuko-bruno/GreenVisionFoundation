from django.db import models

# Create your models here.
# myapp/views.py
# myapp/models.py
from django.db import models

class Contacts(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# myapp/models.py
from django.db import models

class FormData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


