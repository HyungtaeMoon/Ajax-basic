# Generated by Django 2.1.5 on 2019-01-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
