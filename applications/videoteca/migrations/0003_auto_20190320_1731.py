# Generated by Django 2.1.7 on 2019-03-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoteca', '0002_moves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moves',
            name='bboy',
        ),
        migrations.DeleteModel(
            name='Bboy',
        ),
        migrations.DeleteModel(
            name='Moves',
        ),
    ]
