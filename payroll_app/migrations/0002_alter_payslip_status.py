# Generated by Django 5.1.3 on 2024-11-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='status',
            field=models.CharField(default='approved', max_length=20),
        ),
    ]
