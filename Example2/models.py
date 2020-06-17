from django.db import models

# Create your models here.
class Example2(models.Model):
    lastname = models.CharField(max_length = 255, null = False)
    def __ster__(self):
        return self.lastname
    class Meta:
        db_table = 'Example2'