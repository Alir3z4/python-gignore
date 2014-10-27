__version__ = (2014, 10, 0)


def get_version():
    """
    :rtype: str
    """
    return '.'.join(str(i) for i in __version__)


class Gignore(object):
    BASE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/'

    def get_base_url(self):
        """
        :rtype: str
        """
        return self.BASE_URL
