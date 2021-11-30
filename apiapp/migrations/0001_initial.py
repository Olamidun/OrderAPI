# Generated by Django 3.2.9 on 2021-11-30 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='item_image')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=0)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.item')),
            ],
        ),
    ]
