# Generated by Django 4.0.6 on 2022-08-28 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0006_itenscarrinho_complemento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boleto',
            name='boleto',
        ),
        migrations.AddField(
            model_name='boleto',
            name='banco',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]