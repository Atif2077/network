# Generated by Django 5.0.7 on 2024-08-25 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post_statistics_post_alter_user_id_post_comments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics_post',
            name='id',
        ),
        migrations.AddField(
            model_name='statistics_post',
            name='stat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='network.post'),
        ),
        migrations.AlterField(
            model_name='statistics_post',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statistics_post',
            name='likes_no',
            field=models.IntegerField(default=0),
        ),
    ]
