# Generated by Django 3.1.2 on 2021-11-02 06:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='カテゴリ名')),
                ('income', models.BooleanField(default=False, verbose_name='収入フラグ')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('pay_dt', models.DateField(verbose_name='決済日')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.category', verbose_name='カテゴリ')),
            ],
            options={
                'db_table': 'balance',
            },
        ),
    ]
