# Generated by Django 3.2.8 on 2021-10-16 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaDa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200, null=True)),
                ('tr_cost', models.CharField(blank=True, max_length=200, null=True)),
                ('ln_cost', models.CharField(blank=True, max_length=200, null=True)),
                ('ins_cost', models.CharField(blank=True, max_length=200, null=True)),
                ('paid', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], max_length=200)),
                ('emp_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TADA.employee')),
            ],
        ),
    ]