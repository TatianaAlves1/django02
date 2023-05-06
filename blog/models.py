from django.conf import settings
from django.db import models

# Create your models here.
class Autor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    def __str__(self):
       return self.user.get_username()

class Categoria(models.Model):
    nome      = models.CharField(max_length=150)
    descricao = models.TextField()

    def __str__(self) -> str:
        return f'{self.nome}'


class Post(models.Model):
    titulo     = models.CharField(max_length=255,unique=True)
    slug       = models.SlugField(max_length=255,unique=True)
    texto      = models.TextField()
    dt_post    = models.DateField(auto_now_add=True)
    publicacao = models.BooleanField()
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    categoria =  models.ManyToManyField(Categoria, blank=True)  

    def __str__(self) -> str:
        return f'{self.titulo}'    