# Generated by Django 2.0.3 on 2018-08-01 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table2OneToMany.Student')),
            ],
        ),
    ]
