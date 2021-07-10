from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from django.conf import settings
from utilities.exceptions import CustomException


def check_send_email_permission(email):
    email_count = cache.get('{}{}'.format(settings.EMAIL_SEND_COUNT, email), 0)
    if email_count >= settings.MAX_EMAIL_SEND_COUNT:
        raise CustomException(detail=str(_('Max email send reached')), code=403)
    else:
        cache.set('{}{}'.format(settings.EMAIL_SEND_COUNT, email), email_count + 1,
                  timeout=settings.MAX_EMAIL_SEND_TIMEOUT)


def pagination_permission(user, size, index, allowed_size=50):
    if user.is_staff:
        return size, index
    else:
        return size if size < allowed_size else allowed_size, index
