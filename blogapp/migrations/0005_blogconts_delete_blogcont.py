# Generated by Django 4.2.2 on 2023-06-29 04:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0004_blogcont_delete_blogconts'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogconts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_name', models.CharField(max_length=150)),
                ('photo_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Author_name', models.CharField(max_length=50)),
                ('Blog_content', ckeditor.fields.RichTextField(default='about blog content')),
                ('stars', models.IntegerField(default=3)),
                ('Blog_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='blogcont',
        ),
    ]
