# Generated by Django 4.2 on 2023-05-09 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_school_address_delete_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='town',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='my_app.town', verbose_name='Город'),
        ),
    ]
