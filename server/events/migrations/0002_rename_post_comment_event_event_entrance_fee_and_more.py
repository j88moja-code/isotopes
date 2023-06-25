# Generated by Django 4.1.3 on 2023-06-25 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='entrance_fee',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='line_up',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]