# Generated by Django 4.0.2 on 2022-02-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='test',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
