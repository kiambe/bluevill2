# Generated by Django 4.2.3 on 2023-07-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_report_title_alter_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='image_update',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='video_update',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
