from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    contact = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=500, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        self.save()
