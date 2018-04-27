# Generated by Django 2.0.4 on 2018-04-27 17:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('is_trainer', models.BooleanField()),
                ('education', django.contrib.postgres.fields.jsonb.JSONField()),
                ('experience', django.contrib.postgres.fields.jsonb.JSONField()),
                ('is_student', models.BooleanField()),
                ('current_organization', models.TextField()),
                ('official_contact', models.TextField()),
                ('user_profile_basic_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='day3.UserProfileBasic')),
            ],
        ),
    ]
