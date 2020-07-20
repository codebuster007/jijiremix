# Generated by Django 3.0.8 on 2020-07-20 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ormitem',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ORMBuyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=20)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='store.ORMItem')),
            ],
            options={
                'verbose_name': 'Buyer',
                'verbose_name_plural': 'Buyers',
            },
        ),
        migrations.AddField(
            model_name='ormitem',
            name='sold_to',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sold_to', to='store.ORMBuyer'),
            preserve_default=False,
        ),
    ]
