# Generated by Django 3.1.2 on 2020-12-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'answer', 'verbose_name_plural': 'answer'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'Investor type result', 'verbose_name_plural': 'Investor type result'},
        ),
        migrations.AddField(
            model_name='questionslr',
            name='optionE',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_e'),
        ),
        migrations.AddField(
            model_name='questionslr',
            name='textbox',
            field=models.TextField(blank=True, verbose_name='dialogue_box'),
        ),
        migrations.AlterField(
            model_name='questionesg',
            name='optionC',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_c'),
        ),
        migrations.AlterField(
            model_name='questionesg',
            name='optionD',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_d'),
        ),
        migrations.AlterField(
            model_name='questionslr',
            name='optionA',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_a'),
        ),
        migrations.AlterField(
            model_name='questionslr',
            name='optionB',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_b'),
        ),
        migrations.AlterField(
            model_name='questionslr',
            name='optionC',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_c'),
        ),
        migrations.AlterField(
            model_name='questionslr',
            name='optionD',
            field=models.CharField(blank=True, max_length=500, verbose_name='option_d'),
        ),
    ]
