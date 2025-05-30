# Generated by Django 5.2 on 2025-05-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Номер кабинета')),
            ],
            options={
                'verbose_name': 'кабинет',
                'verbose_name_plural': 'кабинеты',
                'db_table': 'cabinet',
                'ordering': ('name',),
            },
        ),
    ]
