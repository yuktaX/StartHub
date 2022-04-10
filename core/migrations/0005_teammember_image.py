

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_startup_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
