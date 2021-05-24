# Generated by Django 3.1.7 on 2021-03-12 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_customuser_sharingcustomuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='GopUser',
            fields=[
                ('sharingcustomuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persons.sharingcustomuser')),
                ('dev', models.CharField(max_length=100)),
            ],
            bases=('persons.sharingcustomuser',),
        ),
    ]
