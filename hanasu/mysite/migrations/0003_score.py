# Generated by Django 4.0.1 on 2022-02-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_rename_score_hiragana_maneki_score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores_max', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
