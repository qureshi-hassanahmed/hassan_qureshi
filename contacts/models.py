from django.db import models

class Contact(models.Model):
    name = models.CharField(null = False, max_length=50, unique=True)
    notes = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=False, unique=True)