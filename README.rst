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



Supported Python Versions
-------------------------

``gignore`` currently can be run on multiple python versions:

* Python 2 (2.7)
* Python 3 (3.2, 3.3, 3.4)
* PyPy


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


Authors
-------

``gignore`` was originally created in the late 2014 at home,
the bedroom division of the Alireza's place somewhere on planet earth maybe.

The PRIMARY AUTHORS are (and/or have been):

* Alireza Savand <alireza.savand@gmail.com>
* François‎

And here is an inevitably incomplete list of MUCH-APPRECIATED CONTRIBUTORS --
people who have submitted patches, reported bugs, added translations, helped
answer newbie questions, and generally made ``gignore`` that much better:

* Alireza Savand <alireza.savand@gmail.com>

A big THANK YOU goes to:

* François‎ for convincing Alireza to start the project.
* Guido van Rossum for creating Python.



License
-------

``gignore`` is distributed under the terms of BSD license.
