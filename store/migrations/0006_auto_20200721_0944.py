# Generated by Django 3.0.8 on 2020-07-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200720_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormitem',
            name='image',
            field=models.ImageField(default='item_gallery/dummy_img.jpg', upload_to='item_gallery/'),
        ),
    ]
