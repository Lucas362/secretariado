from django.contrib.auth.models import User, Group
from rest_framework import serializers
from lista.cadastro.models import Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'nome',
            'cpf',
            'rg',
            'estado_civil',
            'nome_conjuge',
            'data_nascimento',
            'nome_mae',
            'nome_pai',
            'fixo',
            'celular',
            'zap',
            'email',
            'endereco',
            'bairro',
            'cidade',
            'cep',
            'uf',
            'escolaridade',
            'recebimento',
            'cargo',
            'solicitar_credencial',
            'data_batismo_aguas',
            'data_batismo_es',
            'departamento',
            'endereco_igreja',
            'setor',
            'naturalidade',
            'uf_naturalidade',
            'nacionalidade',
            'data_consagracao',
            'curso_teologico',
            'convencao_origem',

        ]

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)