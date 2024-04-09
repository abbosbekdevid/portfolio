from django.db import models

# Create your models here.



class CategoryModel(models.Model):
    name = models.CharField(max_length = 80)
    
    def __str__(self) -> str:
        return f"{self.name}"


class ProjectModel(models.Model):
    name = models.CharField(max_length = 80)
    description = models.TextField()
    poster = models.ImageField(upload_to = "project/")
    link = models.URLField(max_length = 80)
    category = models.ForeignKey(CategoryModel, on_delete = models.PROTECT)
    completed_at = models.DateField(null = True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    

class ProfileModel(models.Model):
    full_name = models.CharField(max_length = 80, verbose_name = "Full")
    bio = models.TextField()
    image = models.ImageField(upload_to = "profile/")
    link = models.URLField()
    
    def __str__(self) -> str:
        return f"{self.id} - {self.full_name}"
    


class SkillModel(models.Model):
    name = models.CharField(max_length = 80)
    percentage = models.IntegerField()
    order = models.IntegerField()
    

class ServiceModel(models.Model):
    name = models.CharField(max_length = 80)
    icon = models.CharField(max_length = 80)
    order = models.IntegerField() 
    description = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.name}"



class BlogModel(models.Model):
    title = models.CharField(max_length = 80)
    published_at = models.DateField(auto_now = True)
    poster = models.ImageField(upload_to = "blog/")
    author = models.CharField(max_length = 80)
    description = models.TextField()    
    view_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
class AboutModel(models.Model):
    body = models.TextField()
    amount = models.FloatField()
    project_count = models.IntegerField() 
    customer_count = models.IntegerField() 
    
    def __str__(self) -> str:
        return f"{self.id}"
