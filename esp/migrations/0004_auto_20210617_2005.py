# Generated by Django 3.2.4 on 2021-06-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esp', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterField(
            model_name='user',
            name='studentID',
            field=models.IntegerField(verbose_name='student ID'),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('chipID', 'studentID')},
        ),
    ]
