# Generated by Django 4.2 on 2025-01-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sachnoi', '0003_delete_textentry_alter_authors_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
