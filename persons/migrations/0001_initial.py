# Generated by Django 3.1.7 on 2021-03-03 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='persons/avatar/%Y/%m', verbose_name='Аватар')),
                ('image', models.ImageField(upload_to='persons/image/%Y/%m')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='Человек')),
            ],
        ),
    ]
