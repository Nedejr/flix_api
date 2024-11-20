# Generated by Django 5.1.3 on 2024-11-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('ARG', 'Argentina'), ('BRAZIL', 'Brasil'), ('USA', 'Estados Unidos')], max_length=100, null=True)),
            ],
        ),
    ]
