# Generated by Django 4.1.1 on 2023-01-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_description_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Описание полное'),
        ),
    ]