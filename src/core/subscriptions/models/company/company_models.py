"""Organization related models."""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Organization address
    """
    class Meta:
        """Override default plural name."""
        verbose_name_plural = "Addresses"

    address_line_one = models.CharField(max_length=255, null=False,
                                        blank=False)
    address_line_two = models.CharField(max_length=255, null=True,
                                        blank=True)
    short_description = models.CharField(max_length=255, null=True,
                                         blank=True)
    email = models.EmailField(_('email address'), max_length=255)
    phone_number = models.IntegerField(blank=False, null=False)
    website = models.CharField(max_length=255, null=False,
                               blank=False)

    def __str__(self):
        if self.address_line_two:
            return self.address_line_one + '\n' + self.address_line_two
        return self.address_line_one
