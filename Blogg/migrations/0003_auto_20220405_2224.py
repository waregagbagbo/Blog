# Generated by Django 3.1.7 on 2022-04-05 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blogg', '0002_auto_20220405_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blogg.profile'),
        ),
    ]
