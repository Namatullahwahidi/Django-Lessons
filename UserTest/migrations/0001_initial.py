# Generated by Django 2.0 on 2020-01-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=75)),
                ('agree', models.BooleanField()),
            ],
        ),
    ]