# Generated by Django 4.1.7 on 2023-02-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_loader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='supervisor_id',
            field=models.PositiveIntegerField(),
        ),
    ]
