# Generated by Django 4.1.4 on 2022-12-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_event_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('UE', 'Upcoming'), ('PE', 'Past')], default='PE', max_length=8),
        ),
    ]
