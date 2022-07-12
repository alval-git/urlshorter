from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ShortUrl(models.Model):
    slug = models.SlugField(verbose_name="слаг", blank=True)
    long_url = models.URLField(verbose_name="сгенерированный короткий url")
    short_url = models.URLField(verbose_name="указанный длинный url")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="хозяин записи")

    def get_absolute_url(self):
        return reverse('short_url_detail', kwargs={'slug': self.slug})
# Create your models here.
