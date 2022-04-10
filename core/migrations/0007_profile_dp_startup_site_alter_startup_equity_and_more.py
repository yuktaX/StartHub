

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_startup_team_startup_teamimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dp',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='startup',
            name='site',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='equity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='gross_margin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='investment',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='net_margin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='profit_pfy',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='profit_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='revenue_pfy',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='revenue_total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='short_term_debt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='valuation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
