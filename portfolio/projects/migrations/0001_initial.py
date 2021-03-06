# Generated by Django 3.0.3 on 2020-04-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('summary', models.CharField(max_length=254)),
                ('description', models.TextField(max_length=254)),
                ('cover_image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
                ('screenshots', models.ImageField(upload_to='')),
            ],
        ),
    ]
