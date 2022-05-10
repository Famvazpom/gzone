from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.timezone import now
from django_resized import ResizedImageField
# Create your models here.

class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    discord = models.CharField(max_length=30)
    apodo = models.CharField(max_length=50)
    avatar = ResizedImageField(null=True,blank=True,upload_to='pics/',size=(300,300))
    biografia = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'


class Post(models.Model):

    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen_banner = models.URLField(blank=True,null=True)
    descripcion = models.TextField()
    autor = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    content = HTMLField()
    slug = models.SlugField(editable=False,unique=True)

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.titulo

    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = slugify(f'{now().strftime("%Y-%m-%d %H:%M:%S")}-{self.titulo}')
        super(Post,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})


