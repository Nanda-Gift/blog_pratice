# Generated by Django 4.2.2 on 2023-06-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_blogconts_delete_blogcont'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogconts',
            name='id',
        ),
        migrations.AlterField(
            model_name='blogconts',
            name='Blog_name',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]