# Generated by Django 4.0 on 2021-12-13 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_alter_ticket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='idevent',
            field=models.AutoField(db_column='idEvent', primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='idticket',
            field=models.AutoField(db_column='idTicket', primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
