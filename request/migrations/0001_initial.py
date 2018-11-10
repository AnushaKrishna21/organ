# Generated by Django 2.1.3 on 2018-11-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='request_details',
            fields=[
                ('req_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('father_name', models.CharField(default=None, max_length=100)),
                ('address', models.CharField(default=None, max_length=200)),
                ('city', models.CharField(default=None, max_length=100)),
                ('state', models.CharField(default=None, max_length=100)),
                ('phno', models.IntegerField(default=None, max_length=15)),
                ('email', models.CharField(default=None, max_length=100)),
                ('age', models.IntegerField(default=None, max_length=5)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default=None, max_length=1)),
                ('blood', models.CharField(default=None, max_length=5)),
                ('organ_name', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
