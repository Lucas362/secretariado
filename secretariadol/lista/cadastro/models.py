from django.db import models

# Create your models here.
class Person(models.Model):
    ESTADO_CIVIL_ESCOLHAS = (
        (1, "Casado"),
        (2, "Divorciado"),
        (3, "Desquitado"),
        (4, "Não Informado"),
        (5, "Outro"),
        (6, "Separado"),
        (7, "Solteiro"),
        (8, "Viúvo"),
    )

    ESCOLARIDADE_ESCOLHAS = (
        (1, "Bacharel"),
        (2, "Fundamental Completo"),
        (3, "Fundamental Incompleto"),
        (4, "Médio Completo"),
        (5, "Médio Incompleto"),
        (6, "Não Informado"),
        (7, "Pós Graduado"),
        (8, "Superior Completo"),
        (9, "Superior Incompleto"),
    )

    RECEBIMENTO_ESCOLHAS = (
        (1, "Carta"),
        (2, "Batismo"),
        (3, "Aclamação"),
    )

    CARGO_ESCOLHAS = (
        (1, "Auxiliar"),
        (2, "Diácono"),
        (3, "Prebítero"),
        (4, "Evangelista"),
        (5, "Pastor"),
    )

    CURSO_ESCOLHAS = (
        (1, "Bacharel"),
        (2, "Básico"),
        (3, "Médio"),
    )

    nome = models.CharField(max_length=100)
    cpf = models.IntegerField(null=True)
    rg = models.CharField(max_length=20, null=True)
    estado_civil = models.IntegerField(choices=ESTADO_CIVIL_ESCOLHAS, default=4)
    nome_conjuge = models.CharField(max_length=100, null=True)
    data_nascimento = models.CharField(max_length=10)
    nome_mae = models.CharField(max_length=100, null=True)
    nome_pai = models.CharField(max_length=100, null=True)
    fixo = models.CharField(max_length=15, null=True)
    celular = models.CharField(max_length=15, null=True)
    zap = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    cep = models.CharField(max_length=10)
    uf = models.CharField(max_length=2, null=True)
    escolaridade = models.IntegerField(choices=ESCOLARIDADE_ESCOLHAS, default=6, null=True)
    recebimento = models.IntegerField(choices=RECEBIMENTO_ESCOLHAS, default=1, null=True)
    cargo =  models.IntegerField(choices=CARGO_ESCOLHAS, default=1, null=True)
    solicitar_credencial = models.BooleanField(default=False)
    data_batismo_aguas = models.CharField(max_length=10, null=True)
    data_batismo_es = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=50, null=True)
    endereco_igreja = models.CharField(max_length=200)
    setor = models.CharField(max_length=4)
    naturalidade = models.CharField(max_length=20, null=True)
    uf_naturalidade = models.CharField(max_length=2, null=True)
    nacionalidade = models.CharField(max_length=20, null=True)
    data_consagracao = models.CharField(max_length=10, null=True)
    curso_teologico = models.IntegerField(choices=CURSO_ESCOLHAS, default=3, null=True)
    convencao_origem = models.CharField(max_length=10, null=True)
