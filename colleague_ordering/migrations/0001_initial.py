# Generated by Django 4.1.6 on 2023-02-16 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Colleague',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('sirname', models.CharField(max_length=100)),
                ('colleagueID', models.CharField(max_length=8)),
                ('status', models.CharField(max_length=100)),
                ('jobfamily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colleague_ordering.position')),
            ],
        ),
    ]
