# Generated by Django 3.0.7 on 2020-06-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200630_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='%y/$m/$d'),
        ),
    ]