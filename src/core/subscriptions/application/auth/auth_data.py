"""Contains data relevant to the auth module."""
from subscriptions.models.auth.models import CountryCode


def get_country_codes():
    """
    Fetches the app's country codes

    Returns:
    codes(list): list of country codes
    """
    codes = CountryCode.objects.all()
    return codes