# Generated by Django 4.2.1 on 2023-05-09 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('number_home', models.CharField(max_length=30, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
                'ordering': ['street'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='my_app.address', verbose_name='Address')),
                ('categories', models.ManyToManyField(to='my_app.category', verbose_name='Categories')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='my_app.town', verbose_name='City')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Phone number')),
                ('email', models.EmailField(max_length=50, verbose_name='Mail')),
                ('additionally_phone', models.CharField(max_length=12, verbose_name='Additional phone number')),
                ('working_mode', models.TextField(verbose_name='Working mode')),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='my_app.school')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
