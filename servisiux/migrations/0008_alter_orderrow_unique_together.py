# Generated by Django 4.0.3 on 2022-03-28 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servisiux', '0007_rename_order_id_orderrow_order_alter_order_status'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderrow',
            unique_together={('service_id', 'order')},
        ),
    ]