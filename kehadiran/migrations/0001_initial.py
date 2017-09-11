# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karyawan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kehadiran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kehadiran', models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti'), ('alpa', 'Tanpa Alasan'), ('hadir', 'Hadir')], max_length=20)),
                ('waktu', models.DateField()),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan')),
            ],
        ),
    ]
