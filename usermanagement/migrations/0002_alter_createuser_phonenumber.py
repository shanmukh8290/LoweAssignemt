# Generated by Django 3.2 on 2021-06-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuser',
            name='phoneNumber',
            field=models.CharField(default='', max_length=10),
        ),
    ]