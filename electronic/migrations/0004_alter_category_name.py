# Generated by Django 4.1.2 on 2022-10-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronic', '0003_electronic_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
    ]
