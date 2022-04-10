

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_startup_pfy'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
