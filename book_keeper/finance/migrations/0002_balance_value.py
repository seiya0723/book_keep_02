# Generated by Django 3.1.2 on 2021-11-02 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='value',
            field=models.IntegerField(default=0, verbose_name='金額'),
            preserve_default=False,
        ),
    ]