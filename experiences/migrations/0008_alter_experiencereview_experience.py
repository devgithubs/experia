# Generated by Django 4.0.1 on 2022-01-18 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0007_alter_experiencereview_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencereview',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='experiences.experiences'),
        ),
    ]
