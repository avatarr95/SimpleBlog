# Generated by Django 3.0.5 on 2020-04-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_auto_20200421_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50), max_length=60),
        ),
    ]
