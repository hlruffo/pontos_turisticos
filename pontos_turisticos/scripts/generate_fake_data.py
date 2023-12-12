import os
import random
import sys

import django
from django.conf import settings
from django.contrib.auth.models import User
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pontos_turisticos.settings')


django.setup()

from atracoes.models import Atracao
from avaliacoes.models import Avaliacao
from comentarios.models import Comentario
from core.models import PontosTuristico
from enderecos.models import Endereco

fake = Faker()

def create_atracoes(N=5):
    for _ in range(N):
        nome = fake.company()
        descricao = fake.text()
        horario_func = "Das " + fake.time() + " às " + fake.time()
        idade_minima = random.randint(0, 18)
        Atracao.objects.create(
            nome=nome,
            descricao=descricao,
            horario_func=horario_func,
            idade_minima=idade_minima
        )
        
def create_users(N=5):
    for _ in range(N):
        username = fake.user_name()
        email = fake.email()
        password = User.objects.make_random_password()
        User.objects.create_user(username=username, email=email, password=password)

def create_comentarios(N=5):
    for _ in range(N):
        usuario = random.choice(User.objects.all())
        comentario = fake.text()
        aprovado = fake.boolean()
        Comentario.objects.create(
            usuario=usuario,
            comentario=comentario,
            aprovado=aprovado
        )

def create_avaliacoes(N=5):
    for _ in range(N):
        user = random.choice(User.objects.all())
        avaliacao = fake.text()
        nota = round(random.uniform(1, 5), 2)
        Avaliacao.objects.create(
            user=user,
            avaliacao=avaliacao,
            nota=nota
        )

def create_enderecos(N=5):
    for _ in range(N):
        linha1 = fake.street_address()
        cidade = fake.city()
        estado = fake.state()
        pais = fake.country()
        Endereco.objects.create(
            linha1=linha1,
            cidade=cidade,
            estado=estado,
            pais=pais
        )
        
        
def add_pontos_turisticos(N):
    for _ in range(N):
        nome = fake.city()
        descricao = fake.text()
        aprovado = fake.boolean()
        endereco = random.choice(Endereco.objects.all())
        
        pt = PontosTuristico.objects.create(
            nome=nome, 
            descricao=descricao,
            aprovado=aprovado,
            endereco=endereco
        )

        # Adicionando relações M2M
        for _ in range(random.randint(1, 5)):  # Adiciona entre 1 e 5 atracoes
            pt.atracoes.add(random.choice(Atracao.objects.all()))
        
        for _ in range(random.randint(1, 5)):  # Adiciona entre 1 e 5 comentarios
            pt.comentarios.add(random.choice(Comentario.objects.all()))
        
        for _ in range(random.randint(1, 5)):  # Adiciona entre 1 e 5 avaliacoes
            pt.avaliacoes.add(random.choice(Avaliacao.objects.all()))

        pt.save()


    

if __name__ == '__main__':
    create_users(10)
    create_atracoes()
    create_comentarios()
    create_avaliacoes()
    create_enderecos()
    add_pontos_turisticos(50)
