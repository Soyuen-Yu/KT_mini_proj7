# Generated by Django 3.2 on 2022-11-22 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0011_rename_checkbox_aimodel_is_using'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='name',
            field=models.TextField(null=True),
        ),
    ]
