# Generated by Django 4.0.3 on 2022-03-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]