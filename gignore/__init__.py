__version__ = (2014, 10, 0)


def get_version():
    """
    :rtype: str
    """
    return '.'.join(str(i) for i in __version__)


class Gignore(object):
    BASE_URL = 'https://raw.githubusercontent.com/github/gitignore/master/'
    name = None
    file_content = None

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

    def set_file_content(self, file_content):
        """
        :type file_content: str
        """
        self.file_content = file_content

    def get_file_content(self):
        """
        :rtype: str
        """
        return self.file_content
