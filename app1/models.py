from django.db import models

class User(models.Model):
    name       = models.CharField(max_length=20)
    email      = models.CharField(max_length=254, unique=True)
    password   = models.CharField(max_length=20)
    mobile     = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name