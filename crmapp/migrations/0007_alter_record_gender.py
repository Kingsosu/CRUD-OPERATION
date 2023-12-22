# Generated by Django 4.2.7 on 2023-12-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0006_alter_record_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=1),
        ),
    ]
