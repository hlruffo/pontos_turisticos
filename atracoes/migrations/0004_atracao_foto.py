# Generated by Django 3.2.18 on 2023-11-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_alter_atracao_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='atracoes'),
        ),
    ]
