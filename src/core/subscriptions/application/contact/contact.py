"""Contact info."""
from subscriptions.models.company.company_models import Address


def get_address_info():
    """
    Returns company's address info (assumes its the first record)
    """
    return Address.objects.all().first()
