from django.db import models

class Usuario(models.Model):
    primeiro_nome = models.CharField(max_length=45)
    ultimo_nome = models.CharField(max_length=45)
    nome_usuario = models.CharField(max_length=45, unique=True)
    cpf = models.CharField(max_length=11, unique=True) # apenas os números
    telefone = models.models.CharField(max_length=11) # apenas os números
    data_nascimento = models.models.DateField()
    #foto_perfil = models.ImageField(
    #    upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    perfil = models.ForeignKey(
        Perfil, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome_usuario

class Perfil(models.Model):
    nome_perfil = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_perfil



class InfoFinanceira(models.Model):
    renda = models.models.DecimalField(max_digits=10, decimal_places=2, null=False)
    divida = models.models.DecimalField(max_digits=10, decimal_places=2, null=False)
    patrimonio = models.models.DecimalField(max_digits=10, decimal_places=2, null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="info_financeira")

    def __str__(self):
        return f"Renda: {self.renda}, Dívida: {self.divida}, Patrimônio: {self.patrimonio}"




