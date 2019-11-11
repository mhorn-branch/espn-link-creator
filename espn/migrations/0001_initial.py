# Generated by Django 2.2.6 on 2019-11-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mvp_code', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('placement_type', models.CharField(max_length=100)),
                ('audience', models.CharField(max_length=100)),
                ('placement_name', models.CharField(max_length=100)),
                ('fallback_url', models.CharField(max_length=100)),
                ('deeplink_path', models.CharField(max_length=100)),
                ('channel', models.CharField(max_length=100)),
                ('campaign', models.CharField(max_length=100)),
                ('desktop_url', models.CharField(max_length=100)),
            ],
        ),
    ]