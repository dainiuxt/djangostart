# Generated by Django 4.0.3 on 2022-03-22 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servisiux', '0002_rename_cmodel_carmodel_model_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderrow',
            options={'verbose_name': 'Row', 'verbose_name_plural': 'Rows'},
        ),
        migrations.RemoveField(
            model_name='orderrow',
            name='service_id',
        ),
        migrations.AddField(
            model_name='orderrow',
            name='service_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='servisiux.service'),
        ),
    ]
