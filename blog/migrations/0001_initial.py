# Generated by Django 3.1.2 on 2020-12-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=60)),
                ('pub_date', models.DateField()),
                ('first_chars', models.CharField(max_length=120)),
            ],
        ),
    ]