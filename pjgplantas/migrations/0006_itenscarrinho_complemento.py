# Generated by Django 4.0.6 on 2022-08-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0005_rename_cpf_pix_cnpj_remove_itenscarrinho_dt_entrega_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscarrinho',
            name='complemento',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]