# Generated by Django 3.0.8 on 2020-07-20 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200720_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormitem',
            name='sold_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_to', to='store.ORMBuyer'),
        ),
    ]
