# Generated by Django 4.2.11 on 2024-04-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='completed_at',
            field=models.DateField(null=True),
        ),
    ]