from pyexpat import model
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50, validators=[MinLengthValidator(2, "Tag name is too short")])
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.CharField(max_length=100,validators=[MinLengthValidator(50, "Excerpt is too short")])
    image = models.ImageField(upload_to="posts",null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(100)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,related_name='posts', null=True)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments", null=True)
   