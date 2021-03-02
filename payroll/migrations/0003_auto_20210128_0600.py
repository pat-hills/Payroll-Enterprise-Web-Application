# Generated by Django 2.2.17 on 2021-01-28 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_auto_20210124_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowanceroll',
            name='allowance_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowance_type', to='organization.ComplianceAllowance'),
        ),
    ]