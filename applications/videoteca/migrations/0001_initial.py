# Generated by Django 2.1.7 on 2019-03-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bboy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Bboy')),
                ('nacionalidad', models.CharField(blank=True, max_length=80, verbose_name='Pais')),
            ],
        ),
    ]
