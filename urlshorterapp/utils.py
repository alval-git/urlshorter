import random
import string

from .models import ShortUrl


def generateShortUrl():
    slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    while (ShortUrl.objects.filter(slug=slug).first()):
        slug = ''.join(random.choices(string.ascii_lowercase+string.digits, k=7))
    return slug
