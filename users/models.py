import random

from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User, send_mail, UserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,
                          username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)

        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username=None, phone_number=None, email=None, password=None, **extra_fields):
        if username is None:
            if email:
                username = email.split('@', 1)[0]
            if phone_number:
                username = random.choice('abcdefghijklmnopqrstuvwxyz') + str(phone_number)[-7:]
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10, 99))

        return self._create_user(username, phone_number, email, password, False, False, **extra_fields)

    def create_superuser(self, username, phone_number, email, password, **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields)

    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('username', max_length=30, unique=True,
                                help_text=
                                'Required. 30 characters or fewer starting with a letter. Letters, digits and underscore only.',
                                validators=[
                                    validators.RegexValidator(r'^[a-zA-Z][a-zA-Z0-9_\.]+$',
                                                              'Enter a valid username starting with a-z. '
                                                              'This value may contain only letters, numbers '
                                                              'and underscore characters.', 'invalid'),
                                ],
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                }
                                )
    first_name = models.CharField('first_name', max_length=20, blank=True)
    last_name = models.CharField('last_name', max_length=20, blank=True)
    email = models.EmailField('email address', unique=True, null=True, blank=True)
    phone_number = models.BigIntegerField('mobile number', unique=True, null=True, blank=True,
                                          validators=[
                                              validators.RegexValidator(r'^989[0-3,9]\d{8}$',
                                                                        ('Enter a valid mobile number.'), 'invalid'),
                                          ],
                                          error_messages={
                                              'unique': ("A user with this mobile number already exists."),
                                          }
                                          )
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_seen = models.DateTimeField('last seen date', null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick_name = models.CharField('nick_name', max_length=20, blank=True)
    avatar = models.ImageField('avatar', blank=True)
    birthday = models.DateField('birthday', null=True, blank=True)

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
        (WEB, 'web'),
        (IOS, 'ios'),
        (ANDROID, 'android'),
    )

    user = models.ForeignKey(User, related_name='device', on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device uuid', null=True)
    last_login = models.DateTimeField('lsat login', null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=WEB)
    device_os = models.CharField('device os', max_length=20, blank=True)
    device_model = models.CharField('device model', max_length=20, blank=True)
    app_version = models.CharField('app version', max_length=20, blank=True)
    created_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'user-devices'
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        unique_together = ('user', 'device_uuid')
