from django.contrib import admin
from .models import *
from django.contrib import admin
admin.site.register(Cidade)
# admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Leitor)
# admin.site.register(Livro)
admin.site.register(Genero)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1 # Número de livros adicionais para adicionar noadmin
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos nalistagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [LivroInline]# Adiciona a tabela de livros noadmin de gêneros
admin.site.register(Livro)
admin.site.register(Autor,AutorAdmin)