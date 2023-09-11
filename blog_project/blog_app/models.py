from django.db import models

# Create your models here.
class Board(models.Model):
    category = models.CharField(max_length=100)
    title =models.CharField(max_length=100)
    content = models.TextField()
    upload_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=200, default = '')