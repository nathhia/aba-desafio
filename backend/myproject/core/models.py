from django.db import models

class FuncionarioManager(models.Manager):
    def create_funcionario(self, title):
        funcionario = self.create(nome=nome, )
        return funcionario

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    departamento = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)

    objects = FuncionarioManager()
