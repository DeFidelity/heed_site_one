# Generated by Django 3.2.4 on 2021-07-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='static/images/default.png', upload_to='static/images', verbose_name='images'),
        ),
    ]
