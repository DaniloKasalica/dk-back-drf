# Generated by Django 3.1.4 on 2021-01-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210110_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellertoken',
            name='token',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
    ]
