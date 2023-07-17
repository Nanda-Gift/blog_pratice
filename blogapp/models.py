from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

# Create your models here.
class blogconts(models.Model):
    Blog_Id=models.AutoField(primary_key=True)
    Blog_name=models.CharField(max_length=150)
    created_by=models.CharField(max_length=100)
    photo_image=models.ImageField(upload_to="images/",blank=True,null=True)
    Blog_post=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    Author_name=models.CharField(max_length=50)
    Blog_content=RichTextField(default="about blog content")
    stars=models.IntegerField(default=3)

    def __str__(self):
        return self.Blog_name