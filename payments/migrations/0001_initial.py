# Generated by Django 3.2 on 2022-07-24 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('descriptions', models.TextField(blank=True, verbose_name='descriptions')),
                ('avatar', models.ImageField(blank=True, upload_to='gateways/', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable ')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'Gateway',
                'verbose_name_plural': 'Gateway',
                'db_table': 'gateways',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='price')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Void'), (10, 'Piad'), (20, 'Error'), (30, 'User Canceled'), (31, 'Refunded')], db_index=True, default=0, verbose_name='status')),
                ('device_uuid', models.CharField(blank=True, max_length=50, verbose_name='device uuid')),
                ('token', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField(db_index=True, validators=[utils.validators.PhoneNumberValidators], verbose_name='phone number')),
                ('comsumed_code', models.PositiveIntegerField(db_index=True, null=True, verbose_name='consumed reference code')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('gateway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='payments.gateway', verbose_name='Gateway')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='subscriptions.package', verbose_name='Package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payment',
            },
        ),
    ]
