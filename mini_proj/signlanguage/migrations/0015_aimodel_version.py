# Generated by Django 3.2 on 2022-11-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0014_merge_0009_auto_20221122_1424_0013_alter_aimodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='version',
            field=models.CharField(default='1.0v', max_length=30),
        ),
    ]
