# Generated by Django 4.2.6 on 2023-10-15 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_remove_referee_candidate_verification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='referees',
        ),
        migrations.RemoveField(
            model_name='referee',
            name='candidates',
        ),
    ]