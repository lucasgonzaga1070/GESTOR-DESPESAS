from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=10, choices=[('receita', 'Receita'), ('despesa', 'Despesa')], default='despesa')

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"
