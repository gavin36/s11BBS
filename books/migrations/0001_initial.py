# Generated by Django 2.0.6 on 2018-06-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('pub_date', models.DateField()),
                ('publish', models.CharField(max_length=32)),
                ('is_pub', models.BooleanField(default=True)),
            ],
        ),
    ]