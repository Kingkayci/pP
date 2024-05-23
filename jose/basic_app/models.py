from django.db import models

# Create your models here.
class ContactForm(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100)
    contact_subject = models.CharField(max_length=100)
    contact_message = models.CharField(max_length=900)