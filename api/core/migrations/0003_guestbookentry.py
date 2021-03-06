# Generated by Django 4.0.2 on 2022-02-25 21:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_examplemodel_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBookEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
