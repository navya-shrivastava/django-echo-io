# Generated by Django 4.2.5 on 2023-10-14 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='community',
            field=models.TextField(default='no community'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(default='no title'),
        ),
    ]