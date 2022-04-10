

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_teammember_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='team',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='teamimage',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
