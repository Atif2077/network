# Generated by Django 5.0.7 on 2024-08-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_remove_statistics_post_id_statistics_post_stat_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes_no',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Statistics_post',
        ),
    ]
