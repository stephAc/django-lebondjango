# Generated by Django 3.0.6 on 2020-06-02 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200603_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
