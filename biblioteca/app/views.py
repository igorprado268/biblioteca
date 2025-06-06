from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Adicionando a importação do messages
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})


class EmprestimoView(View):
      def get(self, request, *args, **kwargs):
          reservas = Emprestimo.objects.all()
          return render(request, 'reserva.html', {'reservas': reservas})


class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})


class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})


class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})

class ConsultaView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()  # Ajuste conforme sua lógica
        return render(request, 'livros.html', {'livros': livros})

class ReservaView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.objects.all()  # Agora, o modelo Emprestimo está definido corretamente
        return render(request, 'reserva.html', {'reservas': reservas})

class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        livro = Livro.objects.get(id=id)
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')  # Success message
        return redirect('livros')
    



