# Generated by Django 3.0.8 on 2020-10-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201005_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcar',
            name='other_options',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='producthouse',
            name='around_house',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='producthouse',
            name='in_house',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
