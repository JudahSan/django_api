# Generated by Django 4.0.3 on 2022-12-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_animedata_anime_type_animedata_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='animedata',
            name='image',
            field=models.ImageField(default='Images/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]