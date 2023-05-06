from django.contrib import admin
from blog.models import Categoria, Post, Autor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Autor)

