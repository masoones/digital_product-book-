# Generated by Django 3.2 on 2022-07-23 06:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer starting with a letter. Letters, digits and underscore only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z][a-zA-Z0-9_\\.]+$', 'Enter a valid username starting with a-z. This value may contain only letters, numbers and underscore characters.', 'invalid')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=20, verbose_name='last_name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('phone_number', models.BigIntegerField(blank=True, error_messages={'unique': 'A user with this mobile number already exists.'}, null=True, unique=True, validators=[django.core.validators.RegexValidator('^989[0-3,9]\\d{8}$', 'Enter a valid mobile number.', 'invalid')], verbose_name='mobile number')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('last_seen', models.DateTimeField(null=True, verbose_name='last seen date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=20, verbose_name='nick_name')),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='avatar')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_uuid', models.UUIDField(null=True, verbose_name='device uuid')),
                ('last_login', models.DateTimeField(null=True, verbose_name='lsat login')),
                ('device_type', models.PositiveSmallIntegerField(choices=[(1, 'web'), (2, 'ios'), (3, 'android')], default=1)),
                ('device_os', models.CharField(blank=True, max_length=20, verbose_name='device os')),
                ('device_model', models.CharField(blank=True, max_length=20, verbose_name='device model')),
                ('app_version', models.CharField(blank=True, max_length=20, verbose_name='app version')),
                ('created_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'db_table': 'user-devices',
                'unique_together': {('user', 'device_uuid')},
            },
        ),
    ]
