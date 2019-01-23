from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from monologue_api.models import Status, Said

import uuid as uuid_lib


def get_default_status_model_object():
    got_obj, _ = Status.objects.get_or_create(
        action="no action",
        emotion="no emotion"
    )
    return got_obj.pk


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)

    screen_name = models.CharField(
        _('アカウントネーム'),
        max_length=50,
        help_text=_('50字以内で表示される名前を決めてください.'),
        validators=[UnicodeUsernameValidator()],
    )
    username = models.CharField(
        _('アカウントID'),
        max_length=31,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("そのアカウントIDを持ったアカウントはすでに存在しています"),
        },
    )
    email = models.EmailField(_('メールアドレス'), unique=True)

    bio = models.TextField(max_length=150, blank=True)

    # Relational keys
    said = models.ForeignKey(Said, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default=get_default_status_model_object,
    )

    origin = models.ImageField(upload_to="static/photos", default="static/photos/fish_jellyfish.png")
    icon = ImageSpecField(
        source="origin",
        processors=[ResizeToFill(256, 256)],
        format='JPEG'
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
