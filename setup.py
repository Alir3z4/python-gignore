from setuptools import setup

setup(
    name='gignore',
    version=".".join(map(str, __import__('gignore').__version__)),
    packages=['gignore', ],
    url='https://github.com/Alir3z4/python-gignore',
    license='BSD',
    author='Alireza Savand',
    author_email='alireza.savand@gmail.com',
    description='Get .gitignore files from github.com/github/gitignore',
    long_description=open('README.rst').read(),
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'License :: OSI Approved :: BSD License',
    ],
)
