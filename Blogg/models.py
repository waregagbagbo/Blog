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

#define the post status to act as the dropdown in the model
STATUS =(
    ('dr','Draft'),
    ('pub','Published'),
    ('pen','Pending'),
)


class Post(models.Model):
    profile = models.ForeignKey(Profile, models.SET_NULL,null=True, blank=True) 
    title = models.CharField(max_length=200,blank=False) 
    slug = models.SlugField(max_length=100,unique=True, null=True) 
    updated_on = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)   
    status = models.CharField(max_length=20, choices=STATUS, default='dr')

    #let us define metadata which will be used to query data 
    class Meta:
        ordering = ['-created_on']


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
    
    

    
    

    

