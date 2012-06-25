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


Managing Your Settings
----------------------

Managing your settings using ``django-skel`` is simple. Follow the rules below,
and you can't go wrong:

1. Place all your 'common' settings in ``settings/common.py``. This includes
   stuff like: Django apps you need to use in all environmnets (development,
   production, etc.), global variables, etc.

2. Place all your development-specific settings in ``settings/dev.py``. 'Nuff
   said.

3. Place all your production-specific settings in ``settings/prod.py``.

4. If you're confused, follow the documentation links! I've heavily documented
   the settings files, and included reference links to all the relevant
   documentation. If you've got a question, or are confused about something,
   consult the docs first!


Storing Static Assets
---------------------

Always place your static assets (images, javascript, css, etc.) into a
sub-directory of your project folder called ``assets``. If your project is
named ``woot``, for instance, then you should place all your static files
inside of ``woot/assets``.

The way I like to organize this is by doing something like::

    $ mkdir woot/assets
    $ cd woot/assets
    $ mkdir {css,js,img}

Then I'll place all my css files in ``woot/assets/css``, my js files in
``woot/assets/js``, and my images into ``woot/assets/img``.

This way, you've got a clear directory hierarchy, and anyone else that looks at
your code will immediately recognize what's going on.


CSS Best Practices
------------------

One really great feature of ``django-skel`` is that it's already optimized for
handling CSS files in the most optimial way possible. What this means for you,
as a developer, is that if you're planning on writing / using CSS in your
Django project, you should keep the following in mind.

When you include a CSS file in your HTML, it normally looks something like
this::

    <html>
      <head>
        <link rel="stylesheet" href="{{ STATIC_URL }}css/style.css" />
      </head>
    </html>

That's great and all, but by doing things that way you'll miss out on a
powerful feature: CSS templating. Wouldn't it be nice if you could use ``{{
STATIC_URL }}`` *inside* of your CSS files as well? That way you could write
nifty rules like::

    body {
      background: url({{ STATIC_URL }}img/omgyea.png);
    }

The above code snippet is great because it will work in both local development
mode (by having Django serve your image locally), as well as production mode
(by having Amazon S3 serve your image through its CDN). To make use of this
awesome functionality, all you have to do is modify your HTML template like
so::

    {% load compress %}
    <html>
      <head>
        {% compress css %}
          <link rel="stylesheet" href="{{ STATIC_URL }}css/style.css" />
        {% endcompress %}
      </head>
    </html>

Using `django-compressor <http://django_compressor.readthedocs.org/en/latest/index.html>`_
you get this functionality out of the box! Behind the scenes, django-compressor
will run your CSS files through the Django templating engine, which allows you
do the cool stuff mentioned above.

As an added benefit, in production mode, it will also minify your CSS files for
you (removing whitespace to save space). But more on that later!


Javascript Best Practices
-------------------------

Much like CSS best practices, ``django-skel`` is optimized for handling
Javascript code in the same way that it does for CSS (see the previous section
for details).

To make use of both the Django templating engine (so that you can use stuff
like ``{{ STATIC_URL }}`` in your Javascript code) as well as Javascript
minification and obfuscation, change your HTML templates from this::

    <html>
      <head>
        <script src="{{ STATIC_URL }}js/script.js" type="text/javascript"></script>
      </head>
    </html>

To this::

    {% load compress %}
    <html>
      <head>
        {% compress js %}
          <script src="{{ STATIC_URL }}js/script.js" type="text/javascript"></script>
        {% endcompress %}
      </head>
    </html>

And that's all there is to it!
