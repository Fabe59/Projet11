# Generated by Django 3.0.6 on 2020-05-18 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('nutrition_grade_fr', models.CharField(blank=True, max_length=1, null=True)),
                ('image_nutrition_url', models.URLField(blank=True, max_length=250, null=True)),
                ('url', models.URLField(blank=True, max_length=250, null=True)),
                ('image_url', models.URLField(blank=True, max_length=250, null=True)),
                ('openff_id', models.BigIntegerField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='food.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
