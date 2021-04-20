# Generated by Django 3.2 on 2021-04-20 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Sort by Chapter',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Progress_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_progress', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sort by progress',
                'ordering': ['-type_of_progress'],
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default='2021-04-20')),
                ('card_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.PROTECT, to='todolist.category')),
                ('progress_type', models.ForeignKey(default='None', on_delete=django.db.models.deletion.PROTECT, to='todolist.progress_type')),
                ('subtitle', models.ForeignKey(default='Oink-oink', on_delete=django.db.models.deletion.PROTECT, to='todolist.chapter')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
