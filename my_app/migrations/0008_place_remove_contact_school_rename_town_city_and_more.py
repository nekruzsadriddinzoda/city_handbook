# Generated by Django 4.2 on 2023-05-09 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_rename_place_contact_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('address', models.CharField(max_length=300, verbose_name='Address')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='my_app.category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Institutions',
                'verbose_name_plural': 'institution',
                'ordering': ['title'],
            },
        ),
        migrations.RemoveField(
            model_name='contact',
            name='school',
        ),
        migrations.RenameModel(
            old_name='Town',
            new_name='City',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.AddField(
            model_name='place',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='my_app.city', verbose_name='City'),
        ),
        migrations.AddField(
            model_name='contact',
            name='place',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='my_app.place'),
            preserve_default=False,
        ),
    ]
