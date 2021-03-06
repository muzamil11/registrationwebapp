# Generated by Django 3.0.5 on 2020-05-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=200)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Contact_Number', models.CharField(max_length=17)),
                ('Roll_Number', models.CharField(max_length=15)),
                ('Department', models.CharField(max_length=200)),
                ('University', models.CharField(max_length=200)),
            ],
        ),
    ]
