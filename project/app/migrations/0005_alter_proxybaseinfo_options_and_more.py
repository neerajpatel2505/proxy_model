# Generated by Django 5.1.4 on 2024-12-28 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_proxybaseinfo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxybaseinfo',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='proxybaseinfo',
            table='ProxyModel',
        ),
    ]
