# Generated by Django 4.1.7 on 2023-03-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploaded_at',
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterModelTable(
            name='file',
            table=None,
        ),
    ]
