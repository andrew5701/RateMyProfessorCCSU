# Generated by Django 4.1.3 on 2022-11-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_courses_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='courses',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.courses'),
        ),
    ]
