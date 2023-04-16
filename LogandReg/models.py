from django.db import models
import re

# Create your models here.

class Customers(models.Model):
    Name=models.TextField(null=False)
    Username=models.TextField(null=True) #optionel
    Email=models.TextField(null=False ,max_length=30)
    password=models.TextField()


    def Email_valid(Email):
        pattern = r'^[a-zA-Z0-9]+([_.+%-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.search(pattern,Email)
        return bool(match)
    
class Session_model(models.Model):
    session_id = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)
   
    

        
