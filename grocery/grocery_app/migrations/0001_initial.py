# Generated by Django 5.0.3 on 2024-04-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='grocery')),
                ('prize', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
