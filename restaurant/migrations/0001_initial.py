# Generated by Django 3.0.5 on 2020-04-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
                ('salary', models.FloatField(default=0.0)),
            ],
        ),
    ]
