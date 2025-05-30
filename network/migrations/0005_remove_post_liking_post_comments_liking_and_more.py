# Generated by Django 5.0.7 on 2024-08-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_post_comments_post_likes_no_delete_statistics_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liking',
        ),
        migrations.AddField(
            model_name='post_comments',
            name='liking',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
