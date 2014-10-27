__version__ = (2014, 10, 0)


def get_version():
    """
    :rtype: str
    """
    return '.'.join(str(i) for i in __version__)


class Gignore(object):
