# Generated by Django 3.2.11 

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livres', '0004_auto_20220302_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
