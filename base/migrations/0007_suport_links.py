# Generated by Django 4.1.2 on 2022-10-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_suport'),
    ]

    operations = [
        migrations.AddField(
            model_name='suport',
            name='links',
            field=models.URLField(blank=True, null=True),
        ),
    ]
