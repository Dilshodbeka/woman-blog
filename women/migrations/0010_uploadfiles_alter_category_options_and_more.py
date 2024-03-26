# Generated by Django 5.0.3 on 2024-03-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_husband_m_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads_model')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategoriya', 'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create'], 'verbose_name': 'Mashhur ayollar', 'verbose_name_plural': 'Mashhur ayollar'},
        ),
        migrations.AlterField(
            model_name='women',
            name='content',
            field=models.TextField(blank=True, verbose_name='mazmuni'),
        ),
        migrations.AlterField(
            model_name='women',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='women',
            name='title',
            field=models.CharField(max_length=255, verbose_name='sarlavha'),
        ),
    ]
