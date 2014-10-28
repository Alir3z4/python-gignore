=======
gignore
=======

.. contents:: Table of contents

Overview
--------

`gignore <https://github.com/Alir3z4/python-gignore/>`_ Get ``.gitignore``
files from `github/gitignore <https://github.com/github/gitignore>`_.

CLI
---

``gignore`` comes with a Command Line Interface and works just like any
other unix based command line application.

The output of ``gignore`` will be echo out to command line and can be simply
pipe to other applications.


Installation
------------
``gignore`` is available on pypi

http://pypi.python.org/pypi/gignore

So easily install it by ``pip``
::
    
    $ pip install gignore

Or by ``easy_install``
::
    
    $ easy_install gignore

Another way is by cloning ``python-gignore``'s `git repo <https://github.com/Alir3z4/python-gignore>`_ ::
    
    $ git clone git://github.com/Alir3z4/python-gignore.git

Then install it by running:
::
    
    $ python setup.py install


Usage
-----

**CLI**

::

    $ gignore Python
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    ....


**Backend**

::

    >>> from gignore import Gignore
    >>> gig = Gignore('Python')
    >>> gig.get_gitignore_file()
    >>> print(gig.get_file_content())
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]

    # C extensions
    *.so

    # Distribution / packaging
    .Python
    # ....
    >>>
