# Generated by Django 3.2.8 on 2021-10-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_locationmodel_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlıq')),
                ('text', models.TextField(verbose_name='Mətin')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='locationmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
