# Generated by Django 4.0 on 2021-12-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_ticket_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='first_name',
            field=models.CharField(max_length=45, verbose_name='Имя'),
        ),
    ]