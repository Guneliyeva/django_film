from django.db import models

# Create your models here.

class Movie(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Muellif")
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Tesvir")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title