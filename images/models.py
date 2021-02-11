from django.db import models
from django.core.files import File
import urllib.request
from tempfile import NamedTemporaryFile
from DjangoAPI.settings import MEDIA_ROOT

class Image(models.Model):
    img = models.ImageField(verbose_name='Изображение', upload_to='pictures', blank=True)
    img_url = models.URLField(verbose_name='URL Изображения', null=True, blank=True)
    rszdimg = models.ImageField(upload_to='resized_pictures', null=True)

    def save(self, *args, **kwargs):
        if self.img_url and not self.img:
            name = self.img_url.split("/")[-1]
            urllib.request.urlretrieve(self.img_url, MEDIA_ROOT + 'pictures/' + name)
            self.img = 'pictures/' + name
            self.save()
        if not self.rszdimg:
            self.rszdimg = self.img
        super(Image, self).save(*args, **kwargs)
