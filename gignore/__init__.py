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
    valid = True
    errors = []

    def __init__(self, name):
        self.set_name(name)
        self.clean_name()

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

    def is_valid(self):
        """
        :rtype: bool
        """
        return self.valid

    def set_valid(self, valid):
        """
        :type valid: bool
        """
        self.valid = valid

    def add_error(self, error_message):
        """
        :type error_message: str
        """
        self.errors.append(error_message)

    def get_errors(self):
        """
        :rtype: list of str
        """
        return self.errors
    def clean_name(self):
        name = self.get_name()

        if name.endswith('.gitignore'):
            self.set_name(name.replace('.gitignore', ''))
