from django.db import models

# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    
    #default_name = "_defaut"
    
    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection
    
    def __str__(self):
        return self.name
    
    
class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
