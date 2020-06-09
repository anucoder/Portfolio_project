# Generated by Django 3.0.3 on 2020-04-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200421_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='summary',
        ),
        migrations.AddField(
            model_name='project',
            name='tagline',
            field=models.CharField(default='Enter a tagline', max_length=1000),
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.CharField(default='Enter a technology', max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshots',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]