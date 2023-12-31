# Generated by Django 4.2.2 on 2023-08-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_name', models.CharField(max_length=30)),
                ('sc_loc', models.CharField(max_length=20)),
                ('sc_principal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_name', models.CharField(max_length=20)),
                ('st_age', models.IntegerField()),
                ('sc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myStudent', to='app.school')),
            ],
        ),
    ]
