# Generated by Django 4.0.6 on 2022-08-29 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0019_remove_comentario_comentario1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='comentario1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='comentario2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='pjgplantas.planta'),
            preserve_default=False,
        ),
    ]
