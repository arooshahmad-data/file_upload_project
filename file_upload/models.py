from django.db import models

from users.models import User

# Create your models here.

class File(models.Model):
    """
        File model ... more to be added
            Field          Description
            - user         represents the user who uploaded the file (FK)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True) 
    file = models.FileField(upload_to='uploads/') 

    def __str__(self):
        return self.title