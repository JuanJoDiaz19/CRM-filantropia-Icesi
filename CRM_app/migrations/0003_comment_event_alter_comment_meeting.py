# Generated by Django 4.1.7 on 2023-11-15 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_app', '0002_rename_coment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.event'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.meeting'),
        ),
    ]
