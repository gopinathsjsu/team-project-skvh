# Generated by Django 4.1.7 on 2023-02-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Business', '0002_alter_plan_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='duration',
            field=models.IntegerField(help_text='duration in days'),
        ),
    ]