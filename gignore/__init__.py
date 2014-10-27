__version__ = (2014, 10, 0)


def get_version():
    """
    :rtype: str
    """
    return '.'.join(str(i) for i in __version__)


class Gignore(object):
    BASE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/'
    name = None

    def get_base_url(self):
        """
        :rtype: str
        """
        return self.BASE_URL

    def set_name(self, name):
        """
        :type name: str
        """
        self.name = name

    def get_name(self):
        """
        :rtype: str
        """
        return self.name
