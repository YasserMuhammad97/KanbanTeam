# Generated by Django 2.0.4 on 2018-04-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
    ]
