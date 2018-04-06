# Generated by Django 2.0.3 on 2018-04-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boodlerunner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='boodleReceiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phoneNumber', models.IntegerField()),
                ('barracks', models.CharField(max_length=10)),
                ('roomNumber', models.IntegerField()),
                ('restaurant', models.CharField(max_length=50)),
                ('timeOfArrival', models.IntegerField()),
                ('additionalInstruction', models.CharField(max_length=250)),
                ('receiverCompany', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='boodleRequest',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('receiverID', models.CharField(max_length=50)),
                ('runnerID', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='boodleRunner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runnerName', models.CharField(max_length=50)),
                ('runnerPhoneNumber', models.IntegerField()),
                ('runnerBarracks', models.CharField(max_length=10)),
                ('runnerCompany', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Welcome',
        ),
    ]
