# Generated by Django 2.2.16 on 2021-12-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте картинку к публикации', null=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
