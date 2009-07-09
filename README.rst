=============================
Educational Technology Center
=============================

This is a website for the Educational Technology Center at Missouri State University in Springfield, Missouri.

The site is made up of a bunch of ReStructuredText documents that are parsed into HTML and embedded into the sites design.


Dependencies
------------

Django (http://www.djangoproject.com/download/)
Docutils (http://pypi.python.org/pypi/docutils/0.4/)


Adding a new page
-----------------

Adding new pages is as simple as making a new document in the docs folder. The url will be http://etc.missouristate.edu/the-documents-name/. You'll need to edit the index file so the main nav points to this new file.
