# Generated by Django 3.2.7 on 2021-09-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakerapp', '0006_auto_20210919_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Address', models.CharField(max_length=256)),
                ('Email', models.EmailField(max_length=32)),
                ('Company', models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
