# Generated by Django 3.2.8 on 2021-10-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_carousel_is_show2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('job', models.CharField(max_length=100, verbose_name='İş')),
                ('message', models.TextField(verbose_name='Şərh')),
                ('image', models.ImageField(upload_to='images/commentcarousels/')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
            ],
            options={
                'verbose_name': 'Rəy slayderi',
                'verbose_name_plural': 'Rəy slayderləri',
            },
        ),
    ]
