# Generated by Django 3.1.6 on 2021-03-10 19:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('melons', '0002_auto_20210310_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comt_card',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='melons.card'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_id',
            field=models.UUIDField(default=uuid.UUID('65286e41-5ce2-40f1-9cbf-25fb3a91bd55'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comt_id',
            field=models.UUIDField(default=uuid.UUID('9354d049-e790-4cca-a996-e17b80a94846'), editable=False, primary_key=True, serialize=False),
        ),
    ]
