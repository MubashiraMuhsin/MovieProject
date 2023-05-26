from django.db import models

# Create your models here.
class movie_details(models.Model):
    movie_name = models.CharField(max_length=250)
    movie_desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='Gallery')


    def __str__(self):
        return self.movie_name