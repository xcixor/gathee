from django.contrib import admin
from subscriptions.models.auth.models import User, CountryCode

admin.site.register(User)
admin.site.register(CountryCode)
