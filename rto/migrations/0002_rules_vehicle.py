# Generated by Django 4.1.5 on 2023-03-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('rule_code', models.CharField(max_length=50)),
                ('rule_desc', models.CharField(blank=True, max_length=100)),
                ('rule_sect', models.CharField(max_length=50, null=True)),
                ('rule_pen', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_no', models.CharField(default=None, max_length=50)),
                ('vehicle_own_name', models.CharField(default=None, max_length=50)),
                ('vehicle_own_contact', models.IntegerField(default=None)),
                ('vehicle_own_add', models.CharField(default=None, max_length=100)),
                ('vehicle_own_email', models.CharField(default=None, max_length=50)),
                ('vehicle_company_name', models.CharField(default=None, max_length=50)),
                ('vehicle_date_reg', models.DateField(default=None)),
                ('vehicle_chassics_no', models.CharField(default=None, max_length=30)),
                ('vehicle_eng_no', models.CharField(default=None, max_length=30)),
                ('vehicle_own_srno', models.IntegerField(default=None)),
                ('vehicle_fuel_use', models.CharField(default=None, max_length=30)),
                ('vehicle_Seat_cap', models.IntegerField(default=None)),
                ('vehicle_model_name', models.CharField(default=None, max_length=50)),
                ('vehicle_created_date', models.DateField(auto_now_add=True)),
                ('vehicle_last_login', models.CharField(default=None, max_length=30)),
            ],
        ),
    ]
