from django.db import models

# Create your models here.        
        
class profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/',default='images/default/user.png', null= True, blank=True)
    
    def __str__(self):
        return str(self.name)
