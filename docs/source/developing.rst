Developing
==========

.. image:: _static/computer-stare.png

Now that you've got your project running locally and the basics covered, let's
talk about development.

``django-skel`` is optimized for a simple workflow:

* Develop code locally on your laptop using SQLite.
* Run your production code remotely on Heroku.
* Upload your static files (css, javascript, images, etc.) to Amazon S3 so that
  they are served extremely fast to your end-users.
* Compress all your static files (css and javascript) so that end-users can
  download them quicker. This also helps prevent copycats from copy+pasting
  your code, since minified code is much more difficult to reverse engineer.

I've found that using this workflow is the most effective way for me to write
code. If your needs differ from mine, you can easily tweak ``django-skel``'s
settings by editing the files found in ``project_name/settings`` to your
liking. All the options you'll find there are documented, and easy to
understand.

With that said, let's discuss development!
