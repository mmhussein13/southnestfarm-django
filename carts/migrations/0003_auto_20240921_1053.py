# Generated by Django 3.1 on 2024-09-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
        ('carts', '0002_auto_20240902_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]
