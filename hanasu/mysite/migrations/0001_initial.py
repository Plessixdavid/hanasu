# Generated by Django 4.0.1 on 2022-02-08 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ideogramm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('romanji', models.CharField(max_length=50, null=True)),
                ('Img_link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ideotype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Maneki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_hiragana', models.IntegerField(blank=True, null=True)),
                ('score_katakana', models.IntegerField(blank=True, null=True)),
                ('description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.documentary')),
                ('ideogramm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.ideogramm')),
            ],
        ),
        migrations.AddField(
            model_name='ideogramm',
            name='ideotype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.ideotype'),
        ),
    ]
