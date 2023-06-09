# Generated by Django 4.1.5 on 2023-04-10 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('narx', models.PositiveIntegerField()),
                ('chegirma', models.PositiveIntegerField()),
                ('brend', models.CharField(max_length=15)),
                ('batafsil', models.CharField(max_length=200)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('holat', models.CharField(max_length=20)),
                ('mavjud', models.BooleanField(default=True)),
                ('bolim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.bolim')),
            ],
        ),
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=200)),
                ('reyting', models.PositiveIntegerField()),
                ('sana', models.DateField()),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.profil')),
            ],
        ),
    ]
