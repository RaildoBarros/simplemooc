# Generated by Django 2.1.2 on 2018-11-09 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20181108_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['number'], 'verbose_name': 'Aula', 'verbose_name_plural': 'Aulas'},
        ),
    ]
