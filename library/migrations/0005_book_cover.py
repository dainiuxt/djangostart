# Generated by Django 4.0.3 on 2022-03-28 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_author_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers', verbose_name='Viršelis'),
        ),
    ]
