# Generated by Django 3.0.6 on 2020-06-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200605_2328'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='saved_articles',
            field=models.ManyToManyField(to='articles.Articles'),
        ),
    ]
