# Generated by Django 3.1.3 on 2020-11-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=10000)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]