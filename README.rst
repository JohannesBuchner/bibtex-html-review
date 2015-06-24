BibTeX Review HTML pages
--------------------------------

Converts BibTeX files to HTML reviews, with linked PDF files.

Features:
----------

* Supports ReStructuredText in review keyword.
* Automatically links PDF files

Usage
------

* Use JabRef to create a .bib library. The LocalCopy plugin is useful to automatically download and associate PDF files.
* Run::

    python bibtohtml.py my.bib && rst2html.py my.rst > my.html

  You may want to set the BIBDIR environment variable to the path of your PDF files.
* Point your web browser to my.html.

Known bugs
------------

* The review must not contain lines which end with ",". Append a space before 
  the line break if you have these.


