# Generated by Django 4.2 on 2023-04-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Username', models.TextField(null=True)),
                ('Email', models.TextField(max_length=30)),
                ('password', models.TextField()),
            ],
        ),
    ]
