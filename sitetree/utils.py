from importlib import import_module
from django import VERSION
from django.core.exceptions import ImproperlyConfigured

DJANGO_VERSION_INT = int('%s%s%s' % VERSION[:3])


def load_class(path):
    """
    Load class from path.
    """

    try:
        mod_name, cls_name = path.rsplit('.', 1)
        mod = import_module(mod_name)
    except AttributeError as e:
        raise ImproperlyConfigured('Error importing {0}: "{1}"'.format(mod_name, e))
    try:
        cls = getattr(mod, cls_name)
    except AttributeError:
        raise ImproperlyConfigured('Module "{0}" does not define a "{1}" class'.format(mod_name, cls_name))
    return cls
