# Generated by Django 4.2.7 on 2023-11-28 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("enderecos", "0001_initial"),
        ("atracoes", "0001_initial"),
        ("avaliacoes", "0001_initial"),
        ("comentarios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PontosTuristico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("descricao", models.TextField()),
                ("aprovado", models.BooleanField(default=False)),
                (
                    "foto",
                    models.ImageField(
                        blank=True, null=True, upload_to="pontos_turisticos"
                    ),
                ),
                ("atracoes", models.ManyToManyField(to="atracoes.atracao")),
                ("avaliacoes", models.ManyToManyField(to="avaliacoes.avaliacao")),
                ("comentarios", models.ManyToManyField(to="comentarios.comentario")),
                (
                    "endereco",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="enderecos.endereco",
                    ),
                ),
            ],
        ),
    ]
