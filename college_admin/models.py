from django.db import models

class register(models.Model):
    en_no = models.TextField(max_length=20,primary_key=True)
    name = models.TextField(max_length=20)
    img = models.ImageField(upload_to="img/")
    attended = models.BooleanField(default=False)
    cap_img = models.ImageField(upload_to='cap_images/')
    
