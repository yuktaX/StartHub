

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_of_funds', models.TextField(blank=True, null=True)),
                ('problem', models.TextField(blank=True, null=True)),
                ('solution', models.TextField(blank=True, null=True)),
                ('edge', models.TextField(blank=True, null=True)),
                ('RModel', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('equity', models.BigIntegerField(blank=True, null=True)),
                ('investment', models.BigIntegerField(blank=True, null=True)),
                ('valuation', models.BigIntegerField(blank=True, null=True)),
                ('pfy', models.IntegerField(blank=True, null=True)),
                ('revenue_pfy', models.BigIntegerField(blank=True, null=True)),
                ('revenue_total', models.BigIntegerField(blank=True, null=True)),
                ('profit_pfy', models.BigIntegerField(blank=True, null=True)),
                ('profit_total', models.BigIntegerField(blank=True, null=True)),
                ('short_term_debt', models.BigIntegerField(blank=True, null=True)),
                ('net_margin', models.BigIntegerField(blank=True, null=True)),
                ('gross_margin', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teammember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.startup')),
            ],
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='core.tag'),
        ),
    ]
