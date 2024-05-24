from django.contrib import admin
from .models.post import Post
from .models.silla import Silla

admin.site.register(Silla)
admin.site.register(Post)
