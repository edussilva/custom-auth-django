# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from .managers import UserManager
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=100, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user '
            'can log into this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objectss = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.name

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name.split(' ')[0]

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=100, blank=True)
    nascimento = models.DateField('Data de nascimento', null=True, blank=True)
    telefone1 = models.CharField('Telefone 1', max_length=32, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=32, blank=True)
    newsletter = models.BooleanField('Newsletter', default=True)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(pre_save, sender=User)
#def nonexistent_user_profile(sender, instance, **kwargs):
#    if not hasattr(instance, 'profile'):
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
