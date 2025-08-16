from django.contrib import admin

# Register your models here.
from .models import Transacao, Categoria

admin.site.register(Transacao)
admin.site.register(Categoria)