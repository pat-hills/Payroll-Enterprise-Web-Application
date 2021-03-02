# Generated by Django 2.2.17 on 2021-01-21 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0003_auto_20210121_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationUploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='organizationUpload/')),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now=True)),
                ('date_time_created', models.DateTimeField(auto_now=True)),
                ('organization_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_upload', to='organization.Organization')),
                ('user_organization_upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_organization_upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]