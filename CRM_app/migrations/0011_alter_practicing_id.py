# Generated by Django 4.2.5 on 2023-09-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_app', '0010_career_gender_meeting_type_allie_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicing',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
