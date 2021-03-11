# Generated by Django 3.1.6 on 2021-03-11 00:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('melons', '0006_auto_20210310_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(default=uuid.UUID('cf0cea0e-ad5b-4700-ab98-b39e11267c2b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(default='Student', max_length=16),
        ),
    ]
