

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_startup_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
