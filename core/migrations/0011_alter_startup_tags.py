

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_startup_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='core.tag'),
        ),
    ]
