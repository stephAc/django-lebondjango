# Generated by Django 3.0.6 on 2020-06-02 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date de parution')),
                ('accepted', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category')),
                ('town', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.Town')),
            ],
            options={
                'verbose_name': 'articles',
                'ordering': ['timestamp'],
            },
        ),
    ]
