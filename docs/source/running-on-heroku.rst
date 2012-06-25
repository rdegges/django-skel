Running on Heroku
=================

Normally, deploying a Django site would make you want to flip your desk:

.. image:: _static/flip.png

Luckily for us, `Heroku <http://www.heroku.com/>`_ has made the process a
complete joy! If you're aren't familiar with Heroku--they are the **best**
web host, and you will love them if you don't already.

``django-skel`` ships with a production ready Heroku configuration module, and
this section will walk you through creating your Heroku app, and getting your
site running in production.

While this section is quite long, don't be intimidated! It's only long because
I'm explaining everything along the way--the reality of it is that deploying
your site this way really only consists of a couple commands.

If you'd like to read some official documentation on the topic, check out
`Heroku's Django documentation <https://devcenter.heroku.com/articles/django>`_.


Step 1 - Create Your Heroku Application
---------------------------------------

The first step in getting your site running on Heroku is, as I'm sure you've
guessed, to create a Heroku app! Let's do it now::

    $ heroku create [your_app_name_here]

If you don't specify an app name, one will be automatically assigned to you. I
like to name my apps explicitly, because I have a bunch of them, and it's a lot
easier to track.

The next thing you'll need to do is push your project code to Heroku. When you
ran the ``heroku create`` command above, the ``heroku`` command added a new Git
remote to your project. To push your code to Heroku, all you do is push to the
``heroku`` remote::

    $ git push heroku master

That will 'deploy' your code straight to Heroku! From now on, whenever you want
to deploy your code, just run this command.


Step 2 - Install the Addons
---------------------------

Now that you've got your Heroku application going, let's install some `Heroku
Addons <https://addons.heroku.com/>`_. Heroku is a modular system. The core of
Heroku allows you to run your code, but doesn't provide any extra
infrastructure services.

To get things like PostgreSQL, memcache, RabbitMQ, etc.--you need to install
Heroku addons to do what you want.

Let's install our required addons now--these addons are all free (you can
upgrade them at any time in the future). ``django-skel`` already supports all
of these, and requires most of them to function::

    $ heroku addons:add cloudamqp:lemur
    $ heroku-postgresql:dev
    $ scheduler:standard
    $ memcache:5mb
    $ newrelic:standard
    $ pgbackups:auto-month
    $ sentry:developer

`cloudamqp <https://addons.heroku.com/cloudamqp>`_ is a hosted RabbitMQ
service. This is what makes our task queueing (via Celery) possible.

`heroku-postgresql <https://addons.heroku.com/heroku-postgresql>`_ is a hosted
PostgreSQL service that kicks ass.

`scheduler <https://addons.heroku.com/scheduler>`_ is a cron replacement.

`memcache <https://addons.heroku.com/memcache>`_ is a hosted memcache service.

`newrelic <https://addons.heroku.com/newrelic>`_ is the best application
monitoring tool ever created.

`pgbackups <https://addons.heroku.com/pgbackups>`_ is an excellent PostgreSQL
backup tool that stores backups automatically to S3, and lets you download and
manage your backups easily.

`sentry <https://addons.heroku.com/sentry>`_ is a pretty neat error aggregation
and searching tool that makes debugging issues simple.

Just for the record, if you'd like to upgrade any of these free addons, you can
do so by running the ``heroku addons:upgrade`` command. For example--to switch
from the free newrelic addon to their paid addon which has lots more features,
you can simply run::

    $ heroku addons:upgrade newrelic:professional

Bam!

The last thing you'll need to do is specify a default PostgreSQL database
(``django-skel`` requires this). To do this, run::

    $ heroku pg:info

And you should see a database name, something like ``HEROKU_POSTGRESQL_NAVY``.
Once you've got that name, run::

    $ heroku pg:promote HEROKU_POSTGRESQL_NAVY

To set your database as the default.


Step 3 - Configure the Environment
----------------------------------

Heroku operates via environment variables. This is the preferred place to store
all those secret things (passwords, API keys, etc.) that you don't want lurking
around your version control system.

``django-skel`` requires several environment variables be set. To set these
variables, run the following commands::

    # Your AWS security credentials:
    $ heroku config:add AWS_ACCESS_KEY_ID=xxx
    $ heroku config:add AWS_SECRET_ACCESS_KEY=xxx
    $ heroku config:add AWS_STORAGE_BUCKET_NAME=xxx

    # Replace 'woot' with the name of your project:
    $ heroku config:add DJANGO_SETTINGS_MODULE=woot.settings.prod

    # A random long (40 characters or so) string:
    $ heroku config:add SECRET_KEY=xxx

.. note::
    Not sure what to use for your ``SECRET_KEY`` setting? You can always do
    something like::

        from random import choice
        print ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

    And copy the resulting string for usage :)

If you'd like to, you can also enable email support out of the box by setting
the optional email environment variables as well::

    $ heroku config:add EMAIL_HOST=xxx
    $ heroku config:add EMAIL_HOST_PASSWORD=xxx
    $ heroku config:add EMAIL_HOST_USER=xxx
    $ heroku config:add EMAIL_PORT=xxx

.. note::
    ``EMAIL_HOST`` and ``EMAIL_PORT`` will default to the proper settings for
    Google apps, so if you're using that--feel free to leave those out.


Step 4 - Spin It Up!
--------------------

Now that everything is configured and ready to go, let's spin up our backend!

Instead of spinning up 'servers', Heroku allows us to spin up 'dynos', which
are essentially locked-down virtual server instances. The ``Procfile`` defined
at the root of your ``django-skel`` project defines our three service types:

* ``web`` - The service that runs our Django application behind gunicorn.
* ``scheduler`` - The service that runs a Celery worker and the Celerybeat
  daemon.
* ``worker`` - The service that runs a Celery worker **only**.


To spin up a web dyno, run: ``heroku scale web=1``. You can confirm that
everything is working by running ``heroku ps`` afterwards. That will run a
single web dyno.

If you'd like run a Celery worker, run: ``heroku scale scheduler=1``. If you
need more than one worker, you can add additional power by spinning up the
``worker`` dynos, via ``heroku scale worker=1``.

.. note::
    No matter what, never **EVER** spin up more than one ``scheduler``. The
    scheduler process runs Celerybeat, which schedules background tasks. Having
    more than one scheduler running can cause serious duplicate task problems.
    Instead, you should always have one ``scheduler`` running, and as many
    ``worker`` instances as you need.

Need to add more web servers? No problem::

    $ heroku scale web=100

Need to add more workers? No problem::

    $ heroku scale worker=100

Need to check and see how many dynos you have running? Easy::

    $ heroku ps


Step 5 - Deploy Your Static Assets
----------------------------------

The last step in successfully deploying your production Django application is
to compress and then upload all your static assets to Amazon S3 (css, js,
images, etc.).

To do this, simply run the following commands::

    $ heroku run python manage.py collectstatic --noinput
    $ heroku run python manage.py compress

And that's it!


Extra Reading
-------------

You are now running a best practices Django website, on top of Heroku, using
Amazon S3 to serve your static content!

If you'd like to learn more about Heroku, scaling, and stuff like that, you
should probably check out `my blog <http://rdegges.com/>`_ because I write
about this stuff all the time >:)

Oh, and also, read `Heroku's documentation <https://devcenter.heroku.com/>`_ :)

Now... Go and be happy!

.. image:: _static/happy-overload.png
