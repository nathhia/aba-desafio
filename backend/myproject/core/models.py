from django.db import models
'''
class Funcionario(models.Model):
	nome = models.CharField(max_length=150)
	idade = models.IntegerField()
	departamento = models.CharField(max_length=150)
	funcao = models.CharField(max_length=150)

	def __init__(self):
		self.nome
		super().__init__(*args, **kwargs)

'''

class FuncionarioManager(models.Manager):
    def create_funcionario(self, title):
        funcionario = self.create(nome=nome, )
        # do something with the book
        return funcionario

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    departamento = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)

    objects = FuncionarioManager()

'''

class Funcionario(models.Model):
	nome = models.CharField(max_length=150)
	idade = models.IntegerField()
	departamento = models.CharField(max_length=150)
	funcao = models.CharField(max_length=150)
	
	 @classmethod
	 def create(cls, nome):
	 	funcionario = cls(nome=nome)
	 	return funcionario
	''' 	

'''
	def __init__(self, nome, idade, departamento, funcao):
		super(Funcionario, self).__init__()
		self.nome = nome
'''