# Generated by Django 3.1.2 on 2020-12-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_auto_20201215_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioninvtype',
            name='id',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='question_id'),
        ),
    ]