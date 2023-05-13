# Generated by Django 4.1.7 on 2023-02-26 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('fname', models.CharField(blank=True, db_column='first_name', max_length=100, null=True)),
                ('lname', models.CharField(blank=True, db_column='last_name', max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('role', models.IntegerField(choices=[(0, 'Admin'), (1, 'Member'), (2, 'Non-member')], default=2)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2023, 2, 26, 8, 32, 50, 516613, tzinfo=datetime.timezone.utc))),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2023, 2, 26, 8, 32, 50, 516622, tzinfo=datetime.timezone.utc))),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'user',
                'unique_together': {('phone',)},
            },
        ),
    ]