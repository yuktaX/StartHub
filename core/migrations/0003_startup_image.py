

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_startup_tag_teammember_startup_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
