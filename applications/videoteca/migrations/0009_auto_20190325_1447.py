# Generated by Django 2.1.7 on 2019-03-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0008_auto_20190320_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='powermove',
            name='bboy',
        ),
        migrations.AddField(
            model_name='bboy',
            name='powermove',
            field=models.ManyToManyField(to='videoteca.Powermove'),
        ),
    ]