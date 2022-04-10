

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_profile_dp_startup_site_alter_startup_equity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='pfy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
