# Generated by Django 3.0.8 on 2020-10-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201003_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthouse',
            name='gas_support',
            field=models.CharField(choices=[('Magistral', 'Magistral'), ('Alohida', 'Alohida'), ('Ulanish imkoniyati bor', 'Ulanish imkoniyati bor'), ('Yoʻq', 'Yoʻq')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='producthouse',
            name='in_house',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
