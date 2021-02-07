# Generated by Django 3.1.5 on 2021-02-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likelion', '0002_auto_20210128_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_grade', models.IntegerField(null=True)),
                ('user_pn', models.CharField(max_length=11)),
                ('user_major', models.CharField(max_length=30)),
                ('user_q1', models.TextField()),
                ('user_q2', models.TextField()),
                ('user_q3', models.TextField()),
                ('user_q4', models.TextField()),
                ('user_pass', models.IntegerField(default=2)),
                ('user_time', models.CharField(default='00:00', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]