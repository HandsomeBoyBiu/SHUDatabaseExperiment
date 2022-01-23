# Generated by Django 3.2.9 on 2022-01-22 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('car_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('car_color', models.CharField(max_length=4)),
                ('car_series', models.CharField(max_length=8)),
                ('car_type', models.CharField(max_length=255)),
                ('belonging', models.CharField(default='None', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=16)),
                ('client_type', models.CharField(max_length=255)),
                ('discount', models.IntegerField()),
                ('contact', models.CharField(max_length=8)),
                ('tel', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='FixMan',
            fields=[
                ('fix_man_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_type', models.CharField(max_length=255)),
                ('unit_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FixTables',
            fields=[
                ('fix_id', models.AutoField(primary_key=True, serialize=False)),
                ('register_time', models.DateField()),
                ('car_id', models.CharField(max_length=16)),
                ('priority', models.CharField(max_length=255)),
                ('fix_type', models.CharField(max_length=255)),
                ('pay', models.CharField(max_length=255)),
                ('in_time', models.DateTimeField()),
                ('clerk_name', models.CharField(max_length=8)),
                ('clerk_id', models.IntegerField()),
                ('est_time', models.DateTimeField()),
                ('describe', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JoinTables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fix_id', models.IntegerField(null=True)),
                ('fix_man_id', models.IntegerField(null=True)),
                ('project_table_id', models.IntegerField(null=True)),
                ('work_time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTable',
            fields=[
                ('project_table_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_type', models.CharField(max_length=255)),
            ],
        ),
    ]
