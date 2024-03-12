from django.db import models

class attending_class(models.Model):
    en_no = models.TextField(max_length=20,primary_key=True)
    attended = models.BooleanField()
