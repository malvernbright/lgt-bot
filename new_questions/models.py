from django.db import models
from django.utils.text import slugify

# Create your models here.

class NewQuestions(models.Model):
    title = models.CharField(max_length=255)
    date_asked = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewQuestions, self).save(*args, **kwargs)