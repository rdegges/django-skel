Getting Started
===============

So you're ready to start your next Django project! Let me be your guide. Over
the next few minutes we'll be taking a magical journey together >:)


Creating a New Project
----------------------

To create your new project, run the following command, substituting ``woot``
for whatever you'd like to name your new project::

    $ django-admin.py startproject --template=https://github.com/rdegges/django-skel/zipball/master woot
    $ cd woot
    $ ls
    docs/  fabfile.py  gunicorn.py.ini  manage.py  Procfile  README.md  reqs/ requirements.txt  woot/  wsgi.py

The next thing you'll probably want to do is remove my project docs::

    $ rm -rf docs README.md

That way you don't get the documentation you're reading right now in your new
project.

Lastly, create a Git repository for your new project, and commit everything::

    $ git init
    Initialized empty Git repository in /home/rdegges/Code/ex/woot/.git/
    $ git add .; git commit -m 'First commit using django-skel!'
    ...

Easy, right?!

.. image:: _static/not-bad.png


Install All the Dependencies!
-----------------------------

Before I start writing code, I like to setup a `virtualenv
<http://www.virtualenv.org/en/latest/index.html>`_ for myself--this allows me
to install all my project dependencies in a local installation, as opposed to
installing all of them globally on my box.

To install the local dependencies (that you'll need to run your site locally),
run the following command::

    $ pip install -r reqs/dev.txt
    ...

.. note::
    If the pip command above fails, it means you're missing some C libraries
    that are required for some of the Python libraries to work. The ones you
    need (on Ubuntu) are:

    * libevent-dev
    * libpq-dev
    * libmemcached-dev
    * zlib1g-dev
    * libssl-dev
    * python-dev
    * build-essential

    I also recommend you install ``postgresql-client``, even though it isn't required.

Bam!

.. image:: _static/happy.png


Running Your Site Locally
-------------------------

Before you start coding, let's bootstrap our SQLite database (for local
development), and test our the Django admin panel just to make sure
everything's working::

    $ python manage.py syncdb
    ...
    $ python manage.py migrate
    ...
    $ python manage.py runserver
    ...

Assuming everything's working, you should now be able to visit
http://localhost:8000/admin/ in your web browser, and log in.

The ``syncdb`` command here just initializes our database, and the ``migrate``
command applies our South migrations.

From now on, whenever you want to run your site locally for testing, you can
follow these standard Django conventions.

.. image:: _static/happy-big-smile.png
