from django.db import models
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255, verbose_name="Тақырып")
    author = models.CharField(max_length=255, verbose_name="Автор", default="noone")
    is_published = models.BooleanField(default=True, verbose_name="Шығарылым")
    place = models.CharField(max_length=255, verbose_name="Шығарылған жері", default=" ")
    date = models.DateField(verbose_name="уақыт", default='01-01-2020')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    desc = models.CharField(max_length=100, verbose_name="туралы", default=" ")

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})