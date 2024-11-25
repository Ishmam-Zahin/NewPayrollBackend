# Generated by Django 5.1.3 on 2024-11-24 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_app', '0007_alter_employee_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('department_name', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('main_payscale', models.IntegerField()),
                ('final_amount', models.IntegerField()),
                ('description', models.JSONField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dptPayslips', to='employee_app.department')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payslips', to='employee_app.employee')),
            ],
        ),
    ]