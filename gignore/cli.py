import argparse
from gignore import get_version, Gignore
from gignore.utils import wrapwrite


def main():
    parser = argparse.ArgumentParser(
        prog='gignore',
        description='Get .gitignore files from github.com/github/gitignore'
    )
    parser.add_argument(
        'name',
        help='Name of the .gitignore file.'
    )
    parser.add_argument(
        '--version',
        '-v',
        action='version',
        version='%(prog)s {0}'.format(get_version()),
        help='show version number',
    )

    args = parser.parse_args()

    giginore_name = str(args.name)

    gig = Gignore(giginore_name)
    gig.get_gitignore_file()

    if gig.is_valid():
        wrapwrite(gig.get_file_content())
    else:
        wrapwrite("{0}\n".format('\n'.join(gig.get_errors())))

