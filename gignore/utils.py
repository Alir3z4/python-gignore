import sys


def wrapwrite(text):
    """
    :type text: str

    :rtype: str
    """
    text = text.encode('utf-8')
    try:  # Python3
        sys.stdout.buffer.write(text)
    except AttributeError:
        sys.stdout.write(text)
