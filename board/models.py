from django.db import models

# Create your models here.

class Math(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return 'subject = {}, content = {}'.format(self.subject, self.content)