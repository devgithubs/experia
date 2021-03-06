# Generated by Django 4.0.1 on 2022-01-17 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_delete_postexperienceview'),
        ('experiences', '0005_alter_experiences_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=200)),
                ('review_rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=100)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiences.experiences')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
