# Generated by Django 2.2.3 on 2019-08-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0003_auto_20190730_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speechscript',
            name='title',
            field=models.CharField(blank=True, max_length=144, null=True, verbose_name='제목'),
        ),
    ]