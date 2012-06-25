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
