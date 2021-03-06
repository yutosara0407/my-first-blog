# Generated by Django 3.1.7 on 2021-04-18 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='サークル')),
            ],
        ),
        migrations.CreateModel(
            name='Gymnasium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='体育館')),
                ('address', models.CharField(max_length=80, verbose_name='体育館住所')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='氏名')),
                ('nickname', models.CharField(max_length=20, verbose_name='ニックネーム')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='メールアドレス')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('circle', models.ManyToManyField(to='myapp.Circle', verbose_name='サークル')),
            ],
        ),
    ]
