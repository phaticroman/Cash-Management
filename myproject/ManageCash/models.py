from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('Human_Resource','Human_Resource'),
        ('Employee','Employee'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)

    
    def __str__(self):   
        
        return f"{self.username}"
    

class AddCash(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.source} - {self.amount}"


class ExpenseModel(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.description}"

