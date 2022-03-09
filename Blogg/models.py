from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username


class Post(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE) 
    title = models.CharField(max_length=200,blank=False) 
    category = models.CharField(max_length=20,blank=False)  
    comments = models.TextField(blank=False)

    def __str__(self):
        return "%s" %(self.title)

    
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s" %(self.name)   

class Book(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=False, upload_to='images',null=True)
    category = models.ForeignKey('Category', blank=False,on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    year_published = models.DateField(null=False)
    price = models.IntegerField()

    def __str__(self):
        return '%s'%(self.name)


class Author(models.Model):
    name = models.CharField(max_length=20)
    year_of_birth = models.DateField()
    country = models.CharField(max_length=20,default='Kenya',blank=False)

    def __str__(self):
        return self.name
    
    

    
    

    

