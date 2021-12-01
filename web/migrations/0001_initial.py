# Generated by Django 3.2.9 on 2021-11-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_gps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('timestamp', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'User_gps',
                'managed': True,
                'unique_together': {('username', 'x', 'y', 'timestamp')},
            },
        ),
    ]
