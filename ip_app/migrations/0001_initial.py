# Generated by Django 5.1.2 on 2024-10-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_performed', models.CharField(choices=[('CREATED', 'create'), ('UPDATED', 'update'), ('DELETED', 'delete')], max_length=10)),
                ('product_name', models.CharField(max_length=100)),
                ('product_id', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('action_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
