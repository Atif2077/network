# Generated by Django 5.1 on 2024-08-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_remove_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics_user',
            name='profile_img',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.Z5BlhFYs_ga1fZnBWkcKjQHaHz?rs=1&pid=ImgDetMain', max_length=2048),
        ),
    ]
