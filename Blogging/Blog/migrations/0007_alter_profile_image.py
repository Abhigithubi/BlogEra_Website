# Generated by Django 4.1.7 on 2023-05-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_customer_profile_alter_blog_blogger_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pic'),
        ),
    ]
