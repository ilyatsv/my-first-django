# Generated by Django 3.0.6 on 2020-05-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20200518_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email_reply_adress',
            field=models.ManyToManyField(blank=True, limit_choices_to={'verified': False}, to='firstapp.Profile'),
        ),
    ]