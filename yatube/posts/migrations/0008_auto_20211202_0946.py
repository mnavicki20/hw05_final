# Generated by Django 2.2.16 on 2021-12-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20211201_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте картинку к публикации', upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
