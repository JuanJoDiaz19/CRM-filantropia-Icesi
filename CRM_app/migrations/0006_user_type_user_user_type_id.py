# Generated by Django 4.2.5 on 2023-11-06 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_app', '0005_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.user_type'),
            preserve_default=False,
        ),
    ]