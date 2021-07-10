import jdatetime
from django.utils import timezone
from datetime import timedelta

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


# ---- Functions -------------#

# this return left time
def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
    return left_time


# token checker if token expired or not
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds=0)


# if token is expired new token will be established
# If token is expired then it will be removed
# and new one with different key will be created
def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(user=token.user)
    return is_expired, token


# ________________________________________________
# DEFAULT_AUTHENTICATION_CLASSES
class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(str(_("Invalid Token")))

        if not token.user.is_active:
            raise AuthenticationFailed(str(_("User is not active")))

        is_expired, token = token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed(str(_("The Token is expired")))

        return (token.user, token)


def convert_to_gregorian(date):
    year = 2018
    month = 1
    day = 1
    jdatetime.date(year, 1, 1).togregorian().year
    return date


def convert_to_jalali(date):
    if date:
        year = date.year
        month = date.month
        day = date.day
        jalali_date = jdatetime.date.fromgregorian(day=day, month=month, year=year)
        return str(jalali_date)


def send_account_activation_email(email, code):
    send_mail(
        str(_("activation code")),
        str(_("Your activation code is: {}")).format(code),
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
