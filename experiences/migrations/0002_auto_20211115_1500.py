# Generated by Django 3.2.8 on 2021-11-15 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experiencecategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='experiences',
            options={'verbose_name_plural': 'Experiences'},
        ),
    ]
