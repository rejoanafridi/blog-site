# Generated by Django 3.0.8 on 2020-10-18 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201017_2319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('published_at', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'PUBLISHED')], default='draft', max_length=10)),
                ('blog_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
            options={
                'ordering': ('published_at',),
            },
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]