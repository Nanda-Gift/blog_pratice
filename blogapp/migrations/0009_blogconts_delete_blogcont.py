# Generated by Django 4.1.3 on 2023-07-17 03:47

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0008_blogcont_blog_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogconts',
            fields=[
                ('Blog_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Blog_name', models.CharField(max_length=150)),
                ('created_by', models.CharField(max_length=100)),
                ('photo_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Author_name', models.CharField(max_length=50)),
                ('Blog_content', ckeditor.fields.RichTextField(default='about blog content')),
                ('stars', models.IntegerField(default=3)),
                ('Blog_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='blogcont',
        ),
    ]