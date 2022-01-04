# Generated by Django 3.2.8 on 2021-12-26 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_auto_20211115_1500'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostExperienceView',
            fields=[
                ('experiences_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='experiences.experiences')),
            ],
            bases=('experiences.experiences', models.Model),
        ),
    ]
