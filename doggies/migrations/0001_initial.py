# Generated by Django 2.1.2 on 2019-04-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField(default=0)),
                ('kid_friendly', models.IntegerField(default=0)),
                ('dog_friendly', models.IntegerField(default=0)),
                ('low_shedding', models.IntegerField(default=0)),
                ('easy_to_groom', models.IntegerField(default=0)),
                ('high_energy', models.IntegerField(default=0)),
                ('good_health', models.IntegerField(default=0)),
                ('low_barking', models.IntegerField(default=0)),
                ('intelligence', models.IntegerField(default=0)),
                ('easy_to_train', models.IntegerField(default=0)),
                ('tolerates_hot', models.IntegerField(default=0)),
                ('tolerates_cold', models.IntegerField(default=0)),
            ],
        ),
    ]
