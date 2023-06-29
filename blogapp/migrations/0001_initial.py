# Generated by Django 4.2.2 on 2023-06-28 08:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogcont',
            fields=[
                ('Blog_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Blog_name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('Author_name', models.CharField(max_length=30)),
                ('Blog_content', ckeditor.fields.RichTextField(default='about blog content')),
                ('stars', models.IntegerField(default=3)),
            ],
        ),
    ]