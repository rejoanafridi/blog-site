# Generated by Django 3.0.8 on 2020-10-28 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20201028_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='connection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Post'),
            preserve_default=False,
        ),
    ]
