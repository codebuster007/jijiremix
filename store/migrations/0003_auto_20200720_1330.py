# Generated by Django 3.0.8 on 2020-07-20 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200720_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormitem',
            name='sold_to',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_to', to='store.ORMBuyer'),
        ),
    ]